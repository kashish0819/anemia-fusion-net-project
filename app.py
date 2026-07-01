import streamlit as st

st.set_page_config(
    page_title="AnemiaFusionNet",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------

st.title("🩸 AnemiaFusionNet")

st.markdown("""
### AI-Powered Multimodal Anemia Screening

Detect anemia using:

- 👁️ Eye Images
- 🩸 Clinical Parameters
- 🌍 Regional Risk Information

Built using deep learning and multimodal feature fusion.
""")

st.divider()

# ---------------------------------------------------------
# FEATURES
# ---------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="card">

## 👁️ Image AI

EfficientNet extracts visual features from
conjunctival eye images.

</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card">

## 🩸 Clinical AI

Analyzes Hemoglobin, MCH, MCHC, MCV and Gender.

</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="card">

## 🌍 Geo Intelligence

Incorporates regional anemia risk for improved prediction.

</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# WORKFLOW
# ---------------------------------------------------------

st.header("How It Works")

c1, c2, c3, c4 = st.columns(4)

c1.info("① Upload Eye Image")
c2.info("② Enter Clinical Data")
c3.info("③ AI Fusion Analysis")
c4.success("④ Receive AI Report")

st.divider()

# ---------------------------------------------------------
# MODEL PERFORMANCE
# ---------------------------------------------------------

st.header("Model Performance")

m1, m2, m3, m4 = st.columns(4)

m1.metric("Validation Accuracy", "83.47%")
m2.metric("Fusion Model", "EfficientNet + Clinical + Geo")
m3.metric("Inputs", "3 Modalities")
m4.metric("Prediction", "< 1 sec")

st.divider()

# ---------------------------------------------------------
# ABOUT
# ---------------------------------------------------------

st.header("About")

st.write("""
AnemiaFusionNet combines computer vision,
clinical laboratory parameters, and regional
risk information into a single deep learning
framework for AI-assisted anemia screening.

The system is intended to support screening
and research. It does not replace professional
medical diagnosis.
""")

st.divider()

# ---------------------------------------------------------
# DISCLAIMER
# ---------------------------------------------------------

st.warning("""
**Medical Disclaimer**

This application is intended for AI-assisted screening,
research, and educational purposes only.
Always consult a qualified healthcare professional
for diagnosis and treatment decisions.
""")

st.success("👉 Select **Prediction** from the left sidebar to begin.")