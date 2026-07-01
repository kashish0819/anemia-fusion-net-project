import streamlit as st
from PIL import Image
from datetime import datetime

# ----------------------------------------
# Page Configuration
# ----------------------------------------

st.set_page_config(
    page_title="AI Prediction | AnemiaFusionNet",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------
# Load Custom CSS
# ----------------------------------------

with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ----------------------------------------
# Sidebar
# ----------------------------------------

st.sidebar.title("🩸 AnemiaFusionNet")

st.sidebar.success("AI Healthcare Platform")

st.sidebar.markdown("---")

st.sidebar.info(
    """
This AI system combines:

• 👁 Eye Image Analysis

• 🩸 Clinical Parameters

• 🌍 Regional Risk

to estimate anemia risk.
"""
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "Version 1.0\n\nFusionNet Research Edition"
)

# ----------------------------------------
# Header
# ----------------------------------------

st.title("🩸 AI Patient Screening")

st.write(
    """
Upload an eye image and provide the patient's clinical
information for AI-assisted anemia screening.
"""
)

st.divider()

# ----------------------------------------
# Patient Information
# ----------------------------------------

st.subheader("👤 Patient Information")

left, right = st.columns(2)

with left:

    patient_name = st.text_input(
        "Patient Name (Optional)"
    )

    age = st.number_input(
        "Age (Optional)",
        min_value=1,
        max_value=120,
        value=25
    )

with right:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    visit_date = st.date_input(
        "Visit Date",
        value=datetime.today()
    )

st.divider()

# ----------------------------------------
# Eye Image Upload
# ----------------------------------------

st.subheader("👁 Upload Eye Image")

uploaded_file = st.file_uploader(
    "Choose an Eye Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Eye Image",
        use_container_width=True
    )

    st.success("✅ Image uploaded successfully.")

else:

    st.info("Please upload an eye image to continue.")

st.divider()

# ----------------------------------------
# Clinical Information
# ----------------------------------------

st.subheader("🩸 Clinical Information")

col1, col2 = st.columns(2)

with col1:

    hb = st.number_input(
        "Hemoglobin (g/dL)",
        min_value=0.0,
        max_value=25.0,
        value=14.0,
        step=0.1
    )

    mch = st.number_input(
        "MCH (pg)",
        min_value=0.0,
        max_value=50.0,
        value=28.0,
        step=0.1
    )

with col2:

    mchc = st.number_input(
        "MCHC (g/dL)",
        min_value=0.0,
        max_value=50.0,
        value=33.0,
        step=0.1
    )

    mcv = st.number_input(
        "MCV (fL)",
        min_value=0.0,
        max_value=150.0,
        value=90.0,
        step=0.1
    )

st.divider()

# ----------------------------------------
# Regional Information
# ----------------------------------------

st.subheader("🌍 Regional Information")

state_geo = {

    "Gujarat":0.82,
    "Maharashtra":0.76,
    "Rajasthan":0.85,
    "Madhya Pradesh":0.87,
    "Uttar Pradesh":0.90,
    "Bihar":0.92,
    "Punjab":0.61,
    "Haryana":0.65,
    "Delhi":0.58,
    "Karnataka":0.68,
    "Tamil Nadu":0.63,
    "Kerala":0.48,
    "West Bengal":0.84,
    "Odisha":0.86,
    "Telangana":0.69,
    "Andhra Pradesh":0.72,
    "Chhattisgarh":0.89,
    "Jharkhand":0.90,
    "Assam":0.83,
    "Jammu & Kashmir":0.70,
    "Goa":0.45,
    "Other":0.75

}

state = st.selectbox(
    "Select State",
    list(state_geo.keys())
)

district = st.text_input(
    "District (Optional)"
)

geo_score = state_geo[state]

risk_level = "Low"

if geo_score >= 0.85:
    risk_level = "High"

elif geo_score >= 0.65:
    risk_level = "Moderate"

geo1, geo2 = st.columns(2)

with geo1:

    st.metric(
        "Geo Risk Score",
        f"{geo_score:.2f}"
    )

with geo2:

    st.metric(
        "Regional Risk",
        risk_level
    )

st.divider()

# ----------------------------------------
# Clinical Summary
# ----------------------------------------

st.subheader("📋 Patient Summary")

summary1, summary2 = st.columns(2)

with summary1:

    st.write(f"**Gender:** {gender}")
    st.write(f"**Hemoglobin:** {hb} g/dL")
    st.write(f"**MCH:** {mch} pg")

with summary2:

    st.write(f"**MCHC:** {mchc} g/dL")
    st.write(f"**MCV:** {mcv} fL")
    st.write(f"**State:** {state}")

st.divider()

# ----------------------------------------
# Analyze Button
# ----------------------------------------

analyze = st.button(
    "🩸 Analyze Patient",
    use_container_width=True
)

# ----------------------------------------
# Prediction
# ----------------------------------------

from ml.predict_fusion import predict_fusion
import time

if analyze:

    if uploaded_file is None:

        st.error("Please upload an eye image before running analysis.")

    else:

        st.divider()

        st.subheader("🤖 AI Analysis")

        progress = st.progress(0)

        status = st.empty()

        steps = [

            "📤 Uploading Image...",
            "👁 Extracting Image Features...",
            "🩸 Processing Clinical Features...",
            "🌍 Calculating Regional Risk...",
            "🧠 Running FusionNet...",
            "📄 Generating Medical Report..."

        ]

        for i, step in enumerate(steps):

            status.info(step)

            progress.progress((i + 1) / len(steps))

            time.sleep(0.4)

        gender_value = 1 if gender == "Male" else 0

        result = predict_fusion(

            uploaded_file,

            gender_value,

            hb,

            mch,

            mchc,

            mcv,

            geo_score

        )

        prediction = result["prediction"]
        confidence = result["confidence"]

        if prediction == 1:

            label = "Anemia"

            icon = "🔴"

        else:

            label = "Normal"

            icon = "🟢"

        if confidence >= 0.90:

            confidence_level = "Very High"

        elif confidence >= 0.75:

            confidence_level = "High"

        elif confidence >= 0.60:

            confidence_level = "Moderate"

        else:

            confidence_level = "Low"

        st.success("✅ Analysis Completed")

        st.divider()

        st.header("🩺 AI Medical Report")

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(

                "Prediction",

                f"{icon} {label}"

            )

        with c2:

            st.metric(

                "Confidence",

                f"{confidence*100:.2f}%"

            )

        with c3:

            st.metric(

                "Geo Risk",

                risk_level

            )

        with c4:

            st.metric(

                "Model",

                "FusionNet"

            )

        st.divider()

        st.subheader("📊 AI Assessment")

        if prediction == 1:

            st.error(

                f"""
### 🔴 High Probability of Anemia

The multimodal FusionNet model estimates a
**{confidence*100:.2f}% probability**
that the patient may have anemia.

The prediction is based on:

- Eye Image Features
- Clinical Parameters
- Regional Risk Information

This result should be confirmed by a healthcare
professional using laboratory investigations.
"""
            )

        else:

            st.success(

                f"""
### 🟢 No Significant Signs of Anemia

The FusionNet model predicts a
**{confidence*100:.2f}% probability**
of a normal condition.

No significant anemia-related patterns were
identified from the provided inputs.

Routine health monitoring is still recommended.
"""
            )

        st.divider()
        
# ----------------------------------------
# Recommended Tests
# ----------------------------------------

st.subheader("🧪 Recommended Laboratory Tests")

if prediction == 1:

    st.info(
        """
✅ Complete Blood Count (CBC)

✅ Serum Ferritin

✅ Serum Iron Profile

✅ Vitamin B12

✅ Folate Level

✅ Peripheral Blood Smear
"""
    )

else:

    st.success(
        """
✅ Routine CBC (if clinically indicated)

✅ Annual Health Check-up

✅ Maintain Healthy Diet

✅ Regular Physical Activity
"""
    )

st.divider()

# ----------------------------------------
# Lifestyle Recommendations
# ----------------------------------------

st.subheader("🥗 Lifestyle Recommendations")

if prediction == 1:

    st.warning(
        """
### Improve Iron Intake

• Eat green leafy vegetables

• Include beans, lentils and legumes

• Consume iron-rich foods

• Increase Vitamin-C intake

• Avoid tea/coffee immediately after meals

• Follow physician recommendations

• Repeat CBC after treatment
"""
    )

else:

    st.success(
        """
### Healthy Lifestyle

• Maintain balanced nutrition

• Stay hydrated

• Exercise regularly

• Get sufficient sleep

• Continue routine health screening
"""
    )

st.divider()

# ----------------------------------------
# AI Summary
# ----------------------------------------

st.subheader("🧠 AI Summary")

summary = f"""
### AI Clinical Interpretation

Prediction : **{label}**

Confidence : **{confidence*100:.2f}%**

Regional Risk : **{risk_level}**

The FusionNet model combines:

• Eye Image Features

• Clinical Parameters

• Regional Risk Information

to estimate anemia risk using multimodal deep learning.

This prediction is intended to support clinical screening and
must not replace professional medical diagnosis.
"""

st.markdown(summary)

st.divider()

# ----------------------------------------
# Download Report
# ----------------------------------------

st.subheader("📄 Download Report")

report = f"""
==============================
AnemiaFusionNet AI Report
==============================

Patient Name : {patient_name if patient_name else "N/A"}

Age : {age}

Gender : {gender}

Visit Date : {visit_date}

--------------------------------

Hemoglobin : {hb}

MCH : {mch}

MCHC : {mchc}

MCV : {mcv}

--------------------------------

State : {state}

District : {district if district else "N/A"}

Geo Risk Score : {geo_score:.2f}

--------------------------------

Prediction : {label}

Confidence : {confidence*100:.2f}%

Regional Risk : {risk_level}

--------------------------------

AI Recommendation

This AI result is generated using the
AnemiaFusionNet multimodal deep learning model.

Please consult a qualified healthcare
professional before making any medical decisions.

--------------------------------

Generated by

AnemiaFusionNet
AI Healthcare Platform
"""

st.download_button(

    label="⬇ Download AI Report",

    data=report,

    file_name="AnemiaFusionNet_Report.txt",

    mime="text/plain"

)

st.divider()

# ----------------------------------------
# Medical Disclaimer
# ----------------------------------------

st.error(
"""
### ⚠ Medical Disclaimer

This application is intended for educational,
research and AI-assisted screening purposes only.

It is **NOT** a substitute for professional medical
diagnosis, laboratory testing or physician advice.

Always consult a qualified healthcare professional
before making healthcare decisions.
"""
)

# ----------------------------------------
# Footer
# ----------------------------------------

st.markdown("---")

st.caption(
"""
© 2026 AnemiaFusionNet

Multimodal AI Framework for Region-Aware Anemia Detection

Developed using PyTorch • Streamlit • EfficientNet • Clinical AI • Geo Intelligence
"""
)