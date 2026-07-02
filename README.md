# 🩸 AnemiaFusionNet

> AI-Powered Multimodal Anemia Detection using Eye Images, Clinical Parameters, and Regional Risk Information

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red)
![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-orange)

---

## 📌 Overview

AnemiaFusionNet is an AI-powered healthcare application designed for rapid and non-invasive anemia screening. The system combines three complementary sources of information:

- 👁️ Conjunctival Eye Images
- 🩸 Clinical Laboratory Parameters
- 🌍 Regional Anemia Risk Information

These heterogeneous data sources are fused using a deep learning framework to improve prediction performance compared to using a single modality.

The project includes a user-friendly Streamlit web application for interactive predictions.

---

# ✨ Features

- Deep learning-based eye image analysis
- Clinical data prediction
- Regional risk feature integration
- Multimodal feature fusion
- Interactive Streamlit interface
- Real-time AI prediction
- Modern responsive dashboard
- Explainable prediction report

---

# 🧠 Model Architecture

The system consists of three independent AI models:

### 👁️ Image Branch
- EfficientNetB0
- Image preprocessing
- Feature extraction

### 🩸 Clinical Branch
Uses laboratory parameters:

- Hemoglobin (Hb)
- MCH
- MCHC
- MCV
- Gender

### 🌍 Geo Branch

Includes regional anemia prevalence information for improving prediction robustness.

### 🔗 Fusion Layer

Outputs from all three branches are concatenated and passed through fully connected layers for final anemia prediction.

---

# 📂 Project Structure

```
AnemiaFusionNet/
│
├── assets/
│   ├── styles.css
│
├── data/
│   ├── clinical/
│   ├── processed/
│   └── eye_image/
│
├── ml/
│   ├── datasets/
│   ├── models/
│   ├── preprocessing/
│   └── fusion/
│
├── notebooks/
│   ├── 01_dataset_analysis.ipynb
│   ├── ...
│   └── 15_streamlit_deployment.ipynb
│
├── pages/
│
├── saved_models/
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 🚀 Technologies Used

- Python
- PyTorch
- EfficientNet
- OpenCV
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib

---

# 📊 Workflow

```
Eye Image
        │
        ▼
 EfficientNet
        │
        ▼
 Image Features
               \
Clinical Data -----> Feature Fusion -----> Prediction
               /
Regional Risk
```

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AnemiaFusionNet.git
```

Move into the project

```bash
cd AnemiaFusionNet
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📈 Model Performance

| Metric | Value |
|---------|--------|
| Validation Accuracy | 83.47% |
| Prediction Time | <1 second |
| Modalities | 3 |
| Framework | Multimodal Deep Learning |

---

# 🖥️ Application

The Streamlit dashboard allows users to:

- Upload conjunctival eye image
- Enter clinical parameters
- Select regional information
- Perform AI prediction
- View prediction report

---

# 📚 Research Pipeline

1. Dataset Analysis
2. Image Preprocessing
3. Clinical Feature Engineering
4. Regional Feature Engineering
5. CNN Model Development
6. Clinical Model Development
7. Geo Model Development
8. Multimodal Feature Fusion
9. Model Training
10. Evaluation
11. Streamlit Deployment

---

# 🎯 Future Improvements

- Mobile application
- Explainable AI (Grad-CAM)
- Cloud deployment
- Multi-language support
- Electronic Health Record integration
- Larger clinical datasets
- Cross-validation experiments

---

# ⚠️ Disclaimer

This application is intended for educational, research, and AI-assisted screening purposes only.

It is **not** a substitute for professional medical diagnosis or treatment. Always consult qualified healthcare professionals for clinical decisions.

---

# 👩‍💻 Author

**Kashish Gupta**

AI | Machine Learning | Deep Learning | Healthcare AI

GitHub: https://github.com/kashish0819

---

# ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork the project

📢 Share it with others

---
