"""
SQLite Database manager for AgriVision Guard detection history.
Provides persistent storage, querying, analytics aggregation, and export.
"""

import sqlite3
import pandas as pd
from datetime import datetime
from pathlib import Path
from config import DB_PATH

def get_connection():
    """Create a connection to the SQLite database."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database schema if it does not already exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS detection_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            crop TEXT NOT NULL,
            condition TEXT NOT NULL,
            confidence REAL NOT NULL,
            severity TEXT NOT NULL,
            category TEXT NOT NULL,
            filename TEXT,
            notes TEXT,
            plot_location TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_detection(crop: str, condition: str, confidence: float, severity: str, 
                  category: str, filename: str = "", notes: str = "", plot_location: str = "Plot 1"):
    """Insert a new detection record into the database."""
    conn = get_connection()
    cursor = conn.cursor()
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO detection_history 
        (timestamp, crop, condition, confidence, severity, category, filename, notes, plot_location)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (now_str, crop, condition, round(confidence, 2), severity, category, filename, notes, plot_location))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def get_all_detections(limit: int = 100, crop_filter: str = None, search_term: str = None):
    """Retrieve detections with optional filtering."""
    conn = get_connection()
    query = "SELECT * FROM detection_history WHERE 1=1"
    params = []
    
    if crop_filter and crop_filter != "All":
        query += " AND crop = ?"
        params.append(crop_filter)
        
    if search_term:
        query += " AND (condition LIKE ? OR notes LIKE ? OR plot_location LIKE ?)"
        wildcard = f"%{search_term}%"
        params.extend([wildcard, wildcard, wildcard])
        
    query += " ORDER BY id DESC LIMIT ?"
    params.append(limit)
    
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_detection_by_id(detection_id: int):
    """Retrieve a single detection record by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM detection_history WHERE id = ?", (detection_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def delete_detection(detection_id: int):
    """Delete a single detection record by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM detection_history WHERE id = ?", (detection_id,))
    conn.commit()
    conn.close()

def clear_all_detections():
    """Clear all records from detection_history table."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM detection_history")
    conn.commit()
    conn.close()

def get_analytics_summary():
    """Compute aggregate statistics for the detection history."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Total count
    cursor.execute("SELECT COUNT(*) FROM detection_history")
    total_count = cursor.fetchone()[0]
    
    if total_count == 0:
        conn.close()
        return {
            "total_count": 0,
            "healthy_count": 0,
            "diseased_count": 0,
            "avg_confidence": 0.0,
            "crop_distribution": {},
            "top_conditions": {},
            "severity_counts": {}
        }
        
    # Healthy vs Diseased
    cursor.execute("SELECT COUNT(*) FROM detection_history WHERE category = 'Healthy'")
    healthy_count = cursor.fetchone()[0]
    diseased_count = total_count - healthy_count
    
    # Average Confidence
    cursor.execute("SELECT AVG(confidence) FROM detection_history")
    avg_confidence = cursor.fetchone()[0] or 0.0
    
    # Crop breakdown
    cursor.execute("SELECT crop, COUNT(*) FROM detection_history GROUP BY crop ORDER BY COUNT(*) DESC")
    crop_distribution = dict(cursor.fetchall())
    
    # Top conditions
    cursor.execute("SELECT condition, COUNT(*) FROM detection_history GROUP BY condition ORDER BY COUNT(*) DESC LIMIT 5")
    top_conditions = dict(cursor.fetchall())
    
    # Severity breakdown
    cursor.execute("SELECT severity, COUNT(*) FROM detection_history GROUP BY severity ORDER BY COUNT(*) DESC")
    severity_counts = dict(cursor.fetchall())
    
    conn.close()
    return {
        "total_count": total_count,
        "healthy_count": healthy_count,
        "diseased_count": diseased_count,
        "avg_confidence": round(avg_confidence, 2),
        "crop_distribution": crop_distribution,
        "top_conditions": top_conditions,
        "severity_counts": severity_counts
    }

def export_history_as_df(crop_filter: str = None) -> pd.DataFrame:
    """Retrieve history as a pandas DataFrame for reporting."""
    detections = get_all_detections(limit=1000, crop_filter=crop_filter)
    if not detections:
        return pd.DataFrame(columns=[
            "ID", "Timestamp", "Crop", "Condition", "Confidence (%)", 
            "Severity", "Category", "Plot Location", "Notes"
        ])
    df = pd.DataFrame(detections)
    df.rename(columns={
        "id": "ID",
        "timestamp": "Timestamp",
        "crop": "Crop",
        "condition": "Condition",
        "confidence": "Confidence (%)",
        "severity": "Severity",
        "category": "Category",
        "plot_location": "Plot Location",
        "notes": "Notes"
    }, inplace=True)
    if "filename" in df.columns:
        df.drop(columns=["filename"], inplace=True)
    return df
