# 🌿 AgriVision Guard: AI-Powered Crop Disease Detection & Care Guidance

An agricultural decision-support web application that classifies crop leaf diseases and provides actionable agronomic management guidance using **TensorFlow**, a pre-trained **MobileNetV2** deep learning architecture, and **Streamlit**, with a persistent **SQLite** field history database.

---

## 🎯 Key Capabilities

- **Multiple Target Crops**: Designed for key crops from the **PlantVillage** dataset:
  - 🍎 **Apple**: Apple Scab, Black Rot (Frog-eye), Cedar Apple Rust, Healthy Foliage.
  - 🌽 **Corn (Maize)**: Gray Leaf Spot (Cercospora), Common Rust, Northern Leaf Blight, Healthy Foliage.
  - 🍇 **Grape**: Black Rot, Esca (Black Measles), Leaf Blight (Isariopsis), Healthy Foliage.
  - 🥔 **Potato**: Early Blight (Target Spots), Late Blight (*Phytophthora infestans*), Healthy Foliage.
  - 🍅 **Tomato**: Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Two-spotted Spider Mite, Target Spot, Tomato Yellow Leaf Curl Virus (TYLCV), Mosaic Virus (ToMV), Healthy Foliage.

- **Deep Learning Vision Engine**:
  - Backbone: **MobileNetV2** with depthwise separable convolutions and inverted linear bottlenecks.
  - Pre-trained on ImageNet with PlantVillage transfer-learning head.
  - High inference efficiency suitable for mobile and edge agricultural computing.
  - Spectral & Optical Foliar Indices: Excess Green Index (ExG), Chlorophyll Vigor, Lesion Area Estimation.

- **Actionable Agronomic Guidance**:
  - Detailed pathogen taxonomy (Fungal, Bacterial, Viral, Oomycete, Acarid).
  - Diagnostic field symptom descriptions and favorable environmental drivers.
  - Integrated Pest & Disease Management (IPM):
    - Cultural & Mechanical controls.
    - Biological & Organic biofungicides / predatory organisms.
    - Chemical controls with active ingredients and FRAC fungicide codes.

- **Field Detection History (SQLite)**:
  - Automatically records timestamp, crop, diagnosed condition, confidence score, severity rating, farm plot location, and scouting notes into `detections.db`.
  - Outbreak analytics and bar charts (scans per crop, most frequent conditions).
  - One-click CSV report export.

- **Insect-Pest Recognition (Extension Roadmap)**:
  - Comprehensive explanation of why insect pest recognition is an architectural extension (multi-instance object detection like YOLOv8 on the IP102 dataset vs leaf classification).
  - Agricultural insect pest dossiers (Fall Armyworm, Spider Mites, Tomato Hornworm, Colorado Potato Beetle, Whiteflies, Codling Moth).
  - Interactive Rule-Based Pest Diagnostic Wizard for rapid field identification.

- **Curated Benchmark Leaf Samples**:
  - Bundled with 16 synthetic and benchmark leaf samples representing healthy leaves and distinct disease pathologies across all 5 crops for instant 1-click testing.

---

## 🏗️ System Architecture

```
crop-disease-detector/
├── app.py                     # Main Streamlit web application
├── config.py                  # PlantVillage classes, crop mappings, constants
├── model_service.py           # MobileNetV2 loader, preprocessing, inference & leaf optics
├── disease_data.py            # Agronomic knowledge base (symptoms, treatments, IPM)
├── database.py                # SQLite database manager for detection history & analytics
├── pest_extension.py          # Pest extension module, dossiers, and diagnostic wizard
├── generate_samples.py        # Generates benchmark leaf images for instant testing
├── requirements.txt           # Python package dependencies
├── README.md                  # Documentation
├── data/
│   └── detections.db          # SQLite persistent database
├── samples/                   # Curated sample leaf images for Apple, Corn, Grape, Potato, Tomato
└── .streamlit/
    └── config.toml            # Agricultural green theme and server configuration
```

---

## 🚀 How to Run the Application

### 1. Open Terminal or PowerShell
Navigate to the project directory:
```bash
cd "C:\Users\Shivam\.gemini\antigravity\scratch\crop-disease-detector"
```

### 2. Install Dependencies (if not already installed)
```bash
pip install -r requirements.txt
```

### 3. Launch the Streamlit Web Application
```bash
streamlit run app.py
```

The application will start and open automatically in your default browser at:
`http://localhost:8501`

---

## 🧪 Testing with Benchmark Samples
No camera or leaf photo ready? 
1. Open the **🔬 Leaf Disease Diagnosis** page.
2. Select **🧪 Select from Curated PlantVillage Benchmark Samples**.
3. Choose any crop condition (e.g., *Tomato - Early Blight*, *Potato - Late Blight*, *Corn - Common Rust*, *Apple - Apple Scab*).
4. Watch the MobileNetV2 model instantly classify the image, display the confidence score, calculate foliar optical indices, and provide treatment recommendations!

---

## ⚠️ Educational Disclaimer
> **Important**: This software is an educational decision-support prototype. It is designed to demonstrate computer vision capabilities in agriculture and does not replace certified laboratory diagnosis, pathogen isolation, or professional on-site advice from licensed agronomists and agricultural extension agents.
