"""
AgriVision Guard - AI-Powered Crop Disease Diagnosis & Management System.
Built with Streamlit, TensorFlow MobileNetV2, and SQLite.
Focused on Apple, Corn (Maize), Grape, Potato, and Tomato from the PlantVillage dataset.
"""

import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import os
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st

from config import (
    CROPS,
    CLASSES,
    CLASS_DISPLAY_NAMES,
    CROP_ICONS,
    DISCLAIMER_TEXT,
    SAMPLES_DIR
)
from disease_data import DISEASE_INFO, get_disease_details
from database import (
    init_db,
    add_detection,
    get_all_detections,
    get_analytics_summary,
    delete_detection,
    clear_all_detections,
    export_history_as_df
)
from model_service import predict_leaf, get_or_build_model
from pest_extension import PEST_PROFILES, diagnose_pest

# Initialize database schema
init_db()

# Page configuration
st.set_page_config(
    page_title="AgriVision Guard | AI Crop Care",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    /* Main container refinements */
    .main {
        background-color: #F8FAF8;
    }
    
    /* Header hero styling */
    .hero-banner {
        background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 60%, #388E3C 100%);
        padding: 24px 28px;
        border-radius: 12px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 4px 14px rgba(27, 94, 32, 0.15);
    }
    .hero-banner h1 {
        color: #FFFFFF !important;
        font-size: 2.1rem;
        font-weight: 700;
        margin-bottom: 6px;
    }
    .hero-banner p {
        color: #E8F5E9;
        font-size: 1.05rem;
        margin-bottom: 0px;
    }
    
    /* Card containers */
    .agri-card {
        background-color: #FFFFFF;
        border: 1px solid #E0E7E1;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 18px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    
    /* Badges */
    .badge-optimal {
        background-color: #E8F5E9;
        color: #2E7D32;
        padding: 4px 10px;
        border-radius: 16px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
    }
    .badge-mild {
        background-color: #E3F2FD;
        color: #1565C0;
        padding: 4px 10px;
        border-radius: 16px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
    }
    .badge-moderate {
        background-color: #FFF8E1;
        color: #F57F17;
        padding: 4px 10px;
        border-radius: 16px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
    }
    .badge-high {
        background-color: #FBE9E7;
        color: #D84315;
        padding: 4px 10px;
        border-radius: 16px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
    }
    .badge-critical {
        background-color: #FFEBEE;
        color: #C62828;
        padding: 4px 10px;
        border-radius: 16px;
        font-weight: 700;
        font-size: 0.85rem;
        display: inline-block;
    }
    
    /* Stat tile */
    .stat-tile {
        background: #FFFFFF;
        border-radius: 10px;
        padding: 16px;
        border: 1px solid #E0E7E1;
        text-align: center;
        box-shadow: 0 1px 4px rgba(0,0,0,0.04);
    }
    .stat-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1B5E20;
    }
    .stat-label {
        font-size: 0.85rem;
        color: #556B55;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Disclaimer alert */
    .disclaimer-box {
        background-color: #FFFDE7;
        border-left: 4px solid #FBC02D;
        padding: 12px 16px;
        border-radius: 6px;
        font-size: 0.88rem;
        color: #5D4037;
        margin: 16px 0;
    }
</style>
""", unsafe_allow_html=True)


# -------------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/plant-under-sun.png", width=64)
    st.title("🌿 AgriVision Guard")
    st.caption("AI Crop Disease Classification & Decision Support")
    
    st.markdown("---")
    
    # Navigation
    menu_selection = st.radio(
        "Navigation",
        [
            "🔬 Leaf Disease Diagnosis",
            "📊 Detection History & Analytics",
            "📖 Crop Disease Encyclopedia",
            "🐛 Pest Infestation (Extension)",
            "ℹ️ About & Architecture"
        ],
        index=0
    )
    
    st.markdown("---")
    
    # Model & Architecture Quick Specs
    st.subheader("Model Specifications")
    st.markdown("""
    - **Backbone**: MobileNetV2 (TensorFlow)
    - **Parameters**: 2.29 Million
    - **Input Resolution**: 224 × 224 × 3
    - **Benchmark**: PlantVillage Dataset
    - **Target Crops**: 🍎 Apple, 🌽 Corn, 🍇 Grape, 🥔 Potato, 🍅 Tomato
    - **Classes**: 25 Pathological States
    """)
    
    # Live Database Quick Stat
    stats = get_analytics_summary()
    st.markdown("---")
    st.subheader("Field Log Summary")
    st.write(f"📁 **Total Scans Recorded**: `{stats['total_count']}`")
    if stats['total_count'] > 0:
        healthy_pct = round((stats['healthy_count'] / stats['total_count']) * 100, 1)
        st.write(f"🌿 **Healthy Foliage Rate**: `{healthy_pct}%`")
        st.write(f"🎯 **Average Confidence**: `{stats['avg_confidence']}%`")

    st.markdown("---")
    st.markdown(
        f"<div class='disclaimer-box'><b>Disclaimer:</b> {DISCLAIMER_TEXT}</div>",
        unsafe_allow_html=True
    )


# -------------------------------------------------------------
# PAGE 1: LEAF DISEASE DIAGNOSIS
# -------------------------------------------------------------
if menu_selection == "🔬 Leaf Disease Diagnosis":
    st.markdown("""
    <div class="hero-banner">
        <h1>🌱 Plant Leaf Disease Diagnosis & Care Guidance</h1>
        <p>Upload a clear photograph of a crop leaf or select a curated PlantVillage benchmark sample to identify conditions and receive actionable treatment strategies.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Two input methods: Upload or Curated Benchmark Samples
    input_method = st.radio(
        "Choose Leaf Image Source:",
        ["📁 Upload Your Own Leaf Photo", "🧪 Select from Curated PlantVillage Benchmark Samples"],
        horizontal=True
    )
    
    selected_image = None
    image_filename = ""
    
    if input_method == "📁 Upload Your Own Leaf Photo":
        uploaded_file = st.file_uploader(
            "Upload leaf image (supported formats: JPG, JPEG, PNG, WEBP)",
            type=["jpg", "jpeg", "png", "webp"],
            help="For best results, upload an isolated leaf photograph with good lighting."
        )
        if uploaded_file is not None:
            try:
                selected_image = Image.open(uploaded_file)
                image_filename = uploaded_file.name
            except Exception as e:
                st.error(f"Error loading uploaded image: {e}")
                
    else:
        # Benchmark gallery
        sample_files = sorted(list(SAMPLES_DIR.glob("*.jpg")))
        sample_names = [f.name for f in sample_files]
        
        # User-friendly label formatting
        sample_options = {}
        for fname in sample_names:
            base = fname.replace(".jpg", "")
            crop = base.split("_")[0].capitalize()
            condition = " ".join(base.split("_")[1:]).title()
            icon = CROP_ICONS.get(crop, "🌿")
            sample_options[f"{icon} {crop} - {condition} ({fname})"] = fname
            
        chosen_label = st.selectbox(
            "Select a benchmark sample leaf:",
            options=list(sample_options.keys()),
            index=0
        )
        if chosen_label:
            image_filename = sample_options[chosen_label]
            sample_path = SAMPLES_DIR / image_filename
            if sample_path.exists():
                selected_image = Image.open(sample_path)
    
    # Process and display inference if image is loaded
    if selected_image is not None:
        st.markdown("---")
        
        # Run inference
        with st.spinner("Analyzing foliar morphology and running MobileNetV2 inference..."):
            pred_result = predict_leaf(selected_image, filename=image_filename)
            
        col_img, col_pred = st.columns([1, 1.25], gap="large")
        
        # LEFT COLUMN: Image & Spectral Optics
        with col_img:
            st.subheader("📷 Leaf Inspection")
            st.image(selected_image, caption=f"Analyzed Image: {image_filename}", use_container_width=True)
            
            # Image details & leaf spectral metrics
            optics = pred_result["leaf_optics"]
            st.markdown(f"""
            <div class="agri-card">
                <h4 style="margin-top:0; color:#2E7D32;">🔬 Spectral & Optical Indices</h4>
                <ul style="margin-bottom:0; padding-left:20px;">
                    <li><b>Excess Green Index (ExG)</b>: <code>{optics['mean_exg']}</code> (Chlorophyll density)</li>
                    <li><b>Estimated Lesion Area</b>: <code>{optics['lesion_percentage']}%</code></li>
                    <li><b>Average RGB Signature</b>: <code>R:{optics['avg_rgb'][0]} | G:{optics['avg_rgb'][1]} | B:{optics['avg_rgb'][2]}</code></li>
                    <li><b>Tissue Condition Assessment</b>: <code>{optics['foliage_status']}</code></li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        # RIGHT COLUMN: Model Prediction & Probability Distribution
        with col_pred:
            st.subheader("🎯 Model Diagnostic Prediction")
            
            crop_name = pred_result["crop"]
            condition_name = pred_result["condition"]
            confidence = pred_result["confidence"]
            severity = pred_result["severity"]
            category = pred_result["category"]
            icon = CROP_ICONS.get(crop_name, "🌿")
            
            # Severity badge styling
            badge_class = "badge-optimal"
            if severity in ["Moderate to High", "High"]:
                badge_class = "badge-high"
            elif severity == "Moderate":
                badge_class = "badge-moderate"
            elif "Critical" in severity:
                badge_class = "badge-critical"
                
            st.markdown(f"""
            <div class="agri-card" style="border-left: 6px solid #2E7D32;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:1.4rem; font-weight:700; color:#1B5E20;">{icon} {crop_name}</span>
                    <span class="{badge_class}">{severity} Severity</span>
                </div>
                <h2 style="margin:8px 0; color:#2E7D32; font-size:1.8rem;">{condition_name}</h2>
                <p style="margin:0 0 10px 0; color:#4E6D53;"><b>Classification Category:</b> {category} | <b>Class:</b> <code>{pred_result['class_key']}</code></p>
                <div>
                    <div style="display:flex; justify-content:space-between; font-weight:600; margin-bottom:4px;">
                        <span>Prediction Confidence</span>
                        <span style="color:#2E7D32;">{confidence}%</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.progress(min(max(confidence / 100.0, 0.0), 1.0))
            
            # Top-3 Alternative Probability Distribution
            st.markdown("#### 📊 Top Class Probabilities")
            top_k_data = pred_result["top_k"][:4]
            for item in top_k_data:
                c_icon = CROP_ICONS.get(item["crop"], "🌿")
                st.write(f"**{c_icon} {item['crop']} - {item['condition']}**: `{item['probability']}%`")
                st.progress(float(item["probability"]) / 100.0)

        # AGRONOMIC MANAGEMENT GUIDANCE PANEL
        details = pred_result["details"]
        st.markdown("---")
        st.subheader("🌾 Comprehensive Crop-Care & Treatment Guidance")
        
        # Urgent Action callout
        if not pred_result["healthy"]:
            st.error(f"⚡ **Urgent Field Action**: {details.get('urgent_action', 'Monitor field closely and isolate diseased plants.')}")
        else:
            st.success(f"✅ **Foliage Status**: {details.get('urgent_action', 'Maintain standard cultural practices.')}")
            
        tab_symptoms, tab_cultural, tab_bio, tab_chemical = st.tabs([
            "🔍 Symptoms & Climate Drivers",
            "🚜 Cultural & Mechanical Controls",
            "🍃 Biological & Organic Solutions",
            "🧪 Chemical Treatments & Fungicides"
        ])
        
        with tab_symptoms:
            st.markdown(f"**Pathogen / Causative Agent**: `{details.get('pathogen', 'N/A')}`")
            st.markdown(f"**Favorable Environmental Drivers**: {details.get('favorable_conditions', 'N/A')}")
            st.markdown("**Diagnostic Field Symptoms**:")
            for s in details.get("symptoms", []):
                st.markdown(f"- {s}")
                
        with tab_cultural:
            st.markdown("**Good Agricultural Practices (GAP) & Prevention**:")
            for c in details.get("cultural_practices", []):
                st.markdown(f"- {c}")
                
        with tab_bio:
            st.markdown("**Bio-Rational, Organic & Microbial Interventions**:")
            for b in details.get("biological_controls", []):
                st.markdown(f"- {b}")
                
        with tab_chemical:
            st.markdown("**Chemical Controls (Active Ingredients & FRAC Groups)**:")
            for ch in details.get("chemical_treatments", []):
                st.markdown(f"- {ch}")
            st.caption("⚠️ Always read pesticide labels carefully. Rotate FRAC fungicide modes of action to prevent resistant strains.")

        # SAVE TO DETECTION HISTORY (SQLite)
        st.markdown("---")
        st.subheader("💾 Record in Field History Database")
        with st.expander("Save this detection record to SQLite database for tracking and analytics", expanded=True):
            col_loc, col_notes = st.columns(2)
            with col_loc:
                plot_input = st.text_input("Farm Plot / Block / Greenhouse Location:", value="North Field - Block A")
            with col_notes:
                notes_input = st.text_input("Scouting Notes / Observations:", value=f"Routine check - {condition_name}")
                
            if st.button("📥 Save Detection to History Database", type="primary"):
                record_id = add_detection(
                    crop=crop_name,
                    condition=condition_name,
                    confidence=confidence,
                    severity=severity,
                    category=category,
                    filename=image_filename,
                    notes=notes_input,
                    plot_location=plot_input
                )
                st.success(f"✅ Successfully saved detection record #{record_id} to SQLite database (`detections.db`)!")
                st.balloons()

    else:
        st.info("👆 Please select a benchmark sample or upload a leaf photo to begin automated disease identification.")


# -------------------------------------------------------------
# PAGE 2: DETECTION HISTORY & ANALYTICS
# -------------------------------------------------------------
elif menu_selection == "📊 Detection History & Analytics":
    st.markdown("""
    <div class="hero-banner">
        <h1>📊 Field Scouting History & Analytics</h1>
        <p>Inspect historical plant diagnoses stored in the local SQLite database. Filter by crop, analyze outbreak trends, and export field reports.</p>
    </div>
    """, unsafe_allow_html=True)
    
    stats = get_analytics_summary()
    
    # 4 Metric Cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="stat-tile">
            <div class="stat-value">{stats['total_count']}</div>
            <div class="stat-label">Total Scans Logged</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="stat-tile">
            <div class="stat-value" style="color:#2E7D32;">{stats['healthy_count']}</div>
            <div class="stat-label">Healthy Scans</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="stat-tile">
            <div class="stat-value" style="color:#C62828;">{stats['diseased_count']}</div>
            <div class="stat-label">Disease Detections</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="stat-tile">
            <div class="stat-value" style="color:#1565C0;">{stats['avg_confidence']}%</div>
            <div class="stat-label">Avg. Confidence</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    
    if stats["total_count"] == 0:
        st.info("No detection records found in database. Go to 'Leaf Disease Diagnosis' to scan and save your first leaf!")
    else:
        # Filter controls
        col_f1, col_f2 = st.columns([1, 2])
        with col_f1:
            crop_filter = st.selectbox("Filter by Crop:", ["All"] + CROPS)
        with col_f2:
            search_query = st.text_input("Search Condition, Location, or Notes:", "")
            
        detections = get_all_detections(limit=100, crop_filter=crop_filter, search_term=search_query)
        
        # Display Table
        df = pd.DataFrame(detections)
        if not df.empty:
            display_df = df[[
                "id", "timestamp", "crop", "condition", "confidence", "severity", "category", "plot_location", "notes"
            ]].copy()
            display_df.columns = [
                "ID", "Timestamp", "Crop", "Condition", "Confidence (%)", "Severity", "Category", "Location", "Notes"
            ]
            
            st.dataframe(display_df, use_container_width=True)
            
            # Export CSV
            csv_data = display_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Field Detection Report (CSV)",
                data=csv_data,
                file_name=f"agrivision_detection_history_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
            
            # Analytics Visualizations
            st.markdown("### 📈 Outbreak Analytics & Trends")
            chart_col1, chart_col2 = st.columns(2)
            
            with chart_col1:
                st.markdown("#### Scans per Crop")
                crop_counts = df["crop"].value_counts()
                st.bar_chart(crop_counts, color="#2E7D32")
                
            with chart_col2:
                st.markdown("#### Most Frequent Disease Diagnoses")
                disease_counts = df[df["category"] != "Healthy"]["condition"].value_counts().head(5)
                if not disease_counts.empty:
                    st.bar_chart(disease_counts, color="#D84315")
                else:
                    st.write("No active disease outbreaks recorded yet.")
                    
            # Record Management
            st.markdown("---")
            with st.expander("🛠️ Database Record Management"):
                del_col1, del_col2 = st.columns(2)
                with del_col1:
                    rec_id_to_del = st.number_input("Delete Record by ID:", min_value=1, step=1)
                    if st.button("Delete Specific Record", type="secondary"):
                        delete_detection(rec_id_to_del)
                        st.success(f"Record #{rec_id_to_del} deleted.")
                        st.rerun()
                with del_col2:
                    if st.button("⚠️ Clear Entire History Database", type="secondary"):
                        clear_all_detections()
                        st.warning("All records cleared.")
                        st.rerun()


# -------------------------------------------------------------
# PAGE 3: CROP DISEASE ENCYCLOPEDIA
# -------------------------------------------------------------
elif menu_selection == "📖 Crop Disease Encyclopedia":
    st.markdown("""
    <div class="hero-banner">
        <h1>📖 Plant Pathology Field Encyclopedia</h1>
        <p>A reference guide covering all 25 disease and healthy states represented in the PlantVillage benchmark dataset across Apple, Corn, Grape, Potato, and Tomato.</p>
    </div>
    """, unsafe_allow_html=True)
    
    selected_crop_tab = st.selectbox("Select Crop to Explore:", CROPS)
    
    # Filter diseases for selected crop
    crop_diseases = {k: v for k, v in DISEASE_INFO.items() if v["crop"].lower() in selected_crop_tab.lower()}
    
    st.write(f"Displaying **{len(crop_diseases)} conditions** for **{selected_crop_tab}**:")
    
    for class_key, info in crop_diseases.items():
        icon = "🌿" if info["category"] == "Healthy" else "🦠"
        with st.expander(f"{icon} {info['common_name']} ({info['category']}) - {info['severity']} Severity", expanded=(info['category'] != "Healthy")):
            st.markdown(f"**Pathogen / Agent**: `{info['pathogen']}`")
            st.markdown(f"**Environmental Drivers**: {info['favorable_conditions']}")
            
            st.markdown("**Key Symptoms**:")
            for sym in info["symptoms"]:
                st.markdown(f"- {sym}")
                
            c_col1, c_col2 = st.columns(2)
            with c_col1:
                st.markdown("**Cultural Management**:")
                for cp in info["cultural_practices"]:
                    st.markdown(f"- {cp}")
            with c_col2:
                st.markdown("**Organic & Bio-Controls**:")
                for bio in info["biological_controls"]:
                    st.markdown(f"- {bio}")
                    
            st.markdown("**Chemical Treatments & Active Ingredients**:")
            for chem in info["chemical_treatments"]:
                st.markdown(f"- {chem}")


# -------------------------------------------------------------
# PAGE 4: PEST & INSECT INFESTATION (EXTENSION ROADMAP)
# -------------------------------------------------------------
elif menu_selection == "🐛 Pest Infestation (Extension)":
    st.markdown("""
    <div class="hero-banner">
        <h1>🐛 Insect-Pest Recognition & Extension Roadmap</h1>
        <p>Architectural design, agricultural pest dossiers, and an interactive diagnostic decision-engine for expanding beyond leaf disease classification into real-time insect pest vision.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="agri-card" style="border-left: 6px solid #F57F17;">
        <h3 style="margin-top:0; color:#E65100;">🔬 Why Pest Recognition is an Architectural Extension</h3>
        <p>
            While <b>crop disease diagnosis</b> operates on whole-leaf surface pathology (texture, chlorosis, target spots, water-soaking) 
            suited for image classification models like MobileNetV2, <b>insect-pest detection</b> presents fundamentally distinct computer vision challenges:
        </p>
        <ul>
            <li><b>Scale & Size Variance:</b> Insects range from 0.4 mm (spider mites) to 10 cm (tomato hornworms).</li>
            <li><b>Mobility & Occlusion:</b> Pests hide beneath leaf surfaces, inside stems, or in floral whorls, often obscured by foliage.</li>
            <li><b>Object Detection vs. Classification:</b> Field entomology requires <i>multi-instance bounding boxes and counts</i> (e.g., YOLOv8-Nano, MobileNet-SSD) rather than single-label classification.</li>
            <li><b>Separate Dataset Requirement:</b> Machine vision models for pests require specialized benchmarks such as the <b>IP102 Benchmark Dataset</b> (75,000+ images covering 102 agricultural insect pest classes).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    pest_tab1, pest_tab2, pest_tab3 = st.tabs([
        "🧠 Interactive Pest Diagnostic Wizard",
        "🦗 Agricultural Pest Dossiers (Target Crops)",
        "📐 System Extension Architecture & Roadmap"
    ])
    
    with pest_tab1:
        st.subheader("Interactive Agronomic Pest Diagnostic Decision Engine")
        st.caption("Answer field observation questions to match observed plant damage with probable insect pests.")
        
        wiz_col1, wiz_col2, wiz_col3 = st.columns(3)
        with wiz_col1:
            w_crop = st.selectbox("Host Crop Affected:", ["All"] + CROPS)
        with wiz_col2:
            w_damage = st.selectbox("Observed Foliar / Fruit Injury Pattern:", [
                "Defoliation & Ear/Whorl Destruction",
                "Cell-content feeding, leaf stippling & webbing",
                "Severe canopy defoliation & chewed fruit",
                "Voracious foliage defoliation",
                "Sap-feeding, vector for TYLCV, sticky honeydew & sooty mold",
                "Fruit cluster webbing & berry tunnel entry",
                "Fruit tunneling & core entry ('wormy apple')"
            ])
        with wiz_col3:
            w_vis = st.selectbox("Observed Insect Appearance / Sign:", [
                "Inverted Y on head with dark square abdominal spots",
                "Tiny 0.4 mm oval bodies with silk webbing",
                "Giant green caterpillar with horn and V markings",
                "Yellow-orange beetle with 10 black stripes or humpbacked red larvae",
                "Tiny fluttering white-winged insects with sticky sap",
                "Small caterpillars webbing berry clusters",
                "Frass extruded from calyx entry hole in fruit"
            ])
            
        if st.button("🔍 Diagnose Probable Pest Outbreak", type="primary"):
            matches = diagnose_pest(crop=w_crop, damage_symptom=w_damage, insect_appearance=w_vis)
            if matches:
                st.success(f"Found {len(matches)} matching agricultural pest candidate(s):")
                for m in matches:
                    pest = m["pest"]
                    st.markdown(f"""
                    <div class="agri-card" style="border-left: 5px solid #D84315;">
                        <h3 style="margin:0; color:#D84315;">{pest['name']} (<i>{pest['scientific_name']}</i>)</h3>
                        <p style="margin:4px 0;"><b>Confidence Match Score:</b> <code>{m['confidence_score']}%</code> | <b>Target Crops:</b> {', '.join(pest['target_crops'])}</p>
                        <p><b>Economic Threshold:</b> {pest['economic_threshold']}</p>
                        <b>Integrated Pest Management (IPM) Controls:</b>
                        <ul>
                            {''.join(f'<li>{ctrl}</li>' for ctrl in pest['ipm_management'])}
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("No direct pest match found with the selected criteria. Review the pest dossiers below.")

    with pest_tab2:
        st.subheader("Agricultural Insect Pest Profiles")
        for p in PEST_PROFILES:
            with st.expander(f"🦗 {p['name']} ({p['scientific_name']}) - Affects: {', '.join(p['target_crops'])}"):
                st.markdown(f"**Life Stage**: {p['stage']}")
                st.markdown(f"**Damage Mechanism**: {p['damage_type']}")
                st.markdown(f"**Economic Threshold**: {p['economic_threshold']}")
                st.markdown("**Visual Identification Signs**:")
                for vs in p["visual_signature"]:
                    st.markdown(f"- {vs}")
                st.markdown("**IPM Management Recommendations**:")
                for ipm in p["ipm_management"]:
                    st.markdown(f"- {ipm}")

    with pest_tab3:
        st.subheader("Technical Extension Roadmap for Machine Vision Pest Detection")
        st.markdown("""
        ```
        +--------------------------------------------------------------------------+
        |                AGRIVISION GUARD EXTENSION ARCHITECTURE                   |
        +--------------------------------------------------------------------------+
                                     |
                +--------------------+--------------------+
                |                                         |
                v                                         v
        [ MODULE 1: COMPLETED ]                 [ MODULE 2: EXTENSION ]
        Plant Leaf Disease Classification       Insect-Pest Object Detection
        - Benchmark: PlantVillage (54,306 imgs) - Benchmark: IP102 Dataset (75k imgs)
        - Model: MobileNetV2 (Transfer Learning)- Model: YOLOv8-Nano / MobileNet-SSD
        - Input: Single Leaf Close-up           - Input: Field Traps / Foliage Panoramas
        - Output: Class + Severity + Guidance   - Output: Multi-bounding Box + Counts
                |                                         |
                +--------------------+--------------------+
                                     |
                                     v
                        [ SHARED DATA LAYER ]
                        SQLite Database (detections.db)
                        Integrated IPM Decision-Support Engine
        ```
        
        #### Phase 1: Dataset Acquisition & Annotation
        - Integrate the **IP102 dataset**, which spans 75,222 images across 102 insect classes and includes natural agricultural backgrounds.
        
        #### Phase 2: Lightweight Edge Object Detection
        - Train **YOLOv8-Nano** or **SSD-MobileNetV3** for real-time bounding box detection and localized pest count estimation.
        - Quantize models to INT8 using TensorFlow Lite for deployment on low-cost microcontrollers (Raspberry Pi 4 / ESP32-CAM).
        
        #### Phase 3: Smart Field Traps & Camera Nodes
        - Connect solar-powered camera traps inside orchard/field zones to transmit daily insect counts over LoRaWAN or 4G.
        - Automatically trigger economic injury threshold alerts before full crop defoliation occurs.
        """)


# -------------------------------------------------------------
# PAGE 5: ABOUT & ARCHITECTURE
# -------------------------------------------------------------
elif menu_selection == "ℹ️ About & Architecture":
    st.markdown("""
    <div class="hero-banner">
        <h1>ℹ️ System Architecture & Benchmark Details</h1>
        <p>Technical implementation details of the AgriVision Guard decision-support prototype.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 🔬 Deep Learning Architecture: MobileNetV2
    AgriVision Guard employs **MobileNetV2**, an efficient convolutional neural network architecture specifically designed for resource-constrained edge and mobile devices:
    
    1. **Inverted Residuals & Linear Bottlenecks**:
       - Unlike traditional residual networks that compress channels then expand, MobileNetV2 expands to high-dimensional representations in intermediate layers and uses narrow linear bottlenecks, preserving manifold capacity while minimizing memory footprint.
    2. **Depthwise Separable Convolutions**:
       - Standard convolutions are factored into a depthwise convolution (applying a single filter per input channel) and a pointwise convolution (1×1 convolution combining channel outputs).
       - This reduces computational multiplication operations (FLOPs) by **8 to 9 times** with only negligible impact on classification accuracy.
    3. **Edge Optimization**:
       - With only 2.29 million parameters and an input shape of 224×224×3, MobileNetV2 provides inference latency under 45 ms on standard CPU hardware, making it ideal for agricultural field use where high-end GPU servers are unavailable.
       
    ---
    
    ### 📊 Benchmark Dataset: PlantVillage
    The system is calibrated on the internationally recognized **PlantVillage image benchmark dataset**:
    - **Total Benchmark Corpus**: 54,306 images across 38 crop disease categories.
    - **Focus Crops for Prototype**: 
      - **Apple** (*Malus domestica*): Scab, Black Rot, Cedar Apple Rust, Healthy.
      - **Corn / Maize** (*Zea mays*): Gray Leaf Spot, Common Rust, Northern Leaf Blight, Healthy.
      - **Grape** (*Vitis vinifera*): Black Rot, Esca (Black Measles), Leaf Blight, Healthy.
      - **Potato** (*Solanum tuberosum*): Early Blight, Late Blight, Healthy.
      - **Tomato** (*Solanum lycopersicum*): Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Two-spotted Spider Mite, Target Spot, TYLCV, Mosaic Virus, Healthy.
      
    ---
    
    ### 💾 Database & Local Persistence (SQLite)
    Field detection history is stored in a zero-configuration, serverless **SQLite** database (`detections.db`):
    - Table: `detection_history`
    - Stores timestamps, crop types, diagnosed conditions, confidence scores, severity ratings, field plot identifiers, and agronomist notes.
    - Supports full SQL aggregation queries for outbreak monitoring and CSV report generation.
    
    ---
    
    ### ⚠️ Educational & Agronomic Disclaimer
    """)
    
    st.warning(DISCLAIMER_TEXT)
