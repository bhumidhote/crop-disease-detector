"""
Configuration file for AgriVision Guard - Crop Leaf Disease Detection System.
Based on crops represented in the PlantVillage image dataset.
"""

import os
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
SAMPLES_DIR = BASE_DIR / "samples"
DB_PATH = DATA_DIR / "detections.db"

# Model Configuration
IMG_SIZE = (224, 224)
INPUT_SHAPE = (224, 224, 3)
MODEL_NAME = "MobileNetV2"
MODEL_WEIGHTS_PATH = DATA_DIR / "plant_village_mobilenetv2.keras"

# Supported Crops
CROPS = [
    "Apple",
    "Corn (Maize)",
    "Grape",
    "Potato",
    "Tomato"
]

# PlantVillage Dataset Classes focused on requested crops
CLASSES = [
    # Apple
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    
    # Corn (Maize)
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    
    # Grape
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    
    # Potato
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    
    # Tomato
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]

NUM_CLASSES = len(CLASSES)

# Human-readable mapping for classes
CLASS_DISPLAY_NAMES = {
    "Apple___Apple_scab": {"crop": "Apple", "condition": "Apple Scab", "healthy": False},
    "Apple___Black_rot": {"crop": "Apple", "condition": "Black Rot (Frog-eye)", "healthy": False},
    "Apple___Cedar_apple_rust": {"crop": "Apple", "condition": "Cedar Apple Rust", "healthy": False},
    "Apple___healthy": {"crop": "Apple", "condition": "Healthy Foliage", "healthy": True},
    
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {"crop": "Corn (Maize)", "condition": "Cercospora / Gray Leaf Spot", "healthy": False},
    "Corn_(maize)___Common_rust_": {"crop": "Corn (Maize)", "condition": "Common Rust", "healthy": False},
    "Corn_(maize)___Northern_Leaf_Blight": {"crop": "Corn (Maize)", "condition": "Northern Leaf Blight", "healthy": False},
    "Corn_(maize)___healthy": {"crop": "Corn (Maize)", "condition": "Healthy Foliage", "healthy": True},
    
    "Grape___Black_rot": {"crop": "Grape", "condition": "Black Rot", "healthy": False},
    "Grape___Esca_(Black_Measles)": {"crop": "Grape", "condition": "Esca (Black Measles)", "healthy": False},
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {"crop": "Grape", "condition": "Leaf Blight (Isariopsis)", "healthy": False},
    "Grape___healthy": {"crop": "Grape", "condition": "Healthy Foliage", "healthy": True},
    
    "Potato___Early_blight": {"crop": "Potato", "condition": "Early Blight", "healthy": False},
    "Potato___Late_blight": {"crop": "Potato", "condition": "Late Blight", "healthy": False},
    "Potato___healthy": {"crop": "Potato", "condition": "Healthy Foliage", "healthy": True},
    
    "Tomato___Bacterial_spot": {"crop": "Tomato", "condition": "Bacterial Spot", "healthy": False},
    "Tomato___Early_blight": {"crop": "Tomato", "condition": "Early Blight", "healthy": False},
    "Tomato___Late_blight": {"crop": "Tomato", "condition": "Late Blight", "healthy": False},
    "Tomato___Leaf_Mold": {"crop": "Tomato", "condition": "Leaf Mold", "healthy": False},
    "Tomato___Septoria_leaf_spot": {"crop": "Tomato", "condition": "Septoria Leaf Spot", "healthy": False},
    "Tomato___Spider_mites Two-spotted_spider_mite": {"crop": "Tomato", "condition": "Two-spotted Spider Mite Damage", "healthy": False},
    "Tomato___Target_Spot": {"crop": "Tomato", "condition": "Target Spot", "healthy": False},
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {"crop": "Tomato", "condition": "Tomato Yellow Leaf Curl Virus", "healthy": False},
    "Tomato___Tomato_mosaic_virus": {"crop": "Tomato", "condition": "Tomato Mosaic Virus", "healthy": False},
    "Tomato___healthy": {"crop": "Tomato", "condition": "Healthy Foliage", "healthy": True}
}

# Crop Emoji icons
CROP_ICONS = {
    "Apple": "🍎",
    "Corn (Maize)": "🌽",
    "Grape": "🍇",
    "Potato": "🥔",
    "Tomato": "🍅"
}

# Educational Disclaimer
DISCLAIMER_TEXT = (
    "Educational Decision-Support Prototype: This system is designed for preliminary screening "
    "and agricultural education using deep learning computer vision on the PlantVillage dataset. "
    "It does not replace certified laboratory diagnosis, pathogen culturing, or on-site consultation "
    "from licensed agronomists and agricultural extension agents."
)
