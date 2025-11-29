import streamlit as st

# Page design
st.set_page_config(page_title="Smart Disease Prediction System", layout="centered")

st.markdown("<h1 style='color:yellow; text-align:center;'>🧠 Smart Disease Prediction System</h1>", unsafe_allow_html=True)

# Disease data
disease_data = {
    "Dengue": {
        "symptoms": ["fever", "headache", "body pain", "vomiting"],
        "medicines": ["Paracetamol", "ORS", "Platelet monitoring"],
        "alert": "High - Doctor Required"
    },
    "Malaria": {
        "symptoms": ["fever", "chills", "sweating", "headache"],
        "medicines": ["Chloroquine", "Paracetamol"],
        "alert": "Medium - Doctor Check-Up Advised"
    },
    "COVID-19": {
        "symptoms": ["fever", "cough", "breathing problem", "loss of taste"],
        "medicines": ["Paracetamol", "Steam Inhalation", "Vitamin C"],
        "alert": "High - Doctor Required"
    },
    "Flu": {
        "symptoms": ["fever", "cold", "sore throat", "headache"],
        "medicines": ["Paracetamol", "Cough Syrup"],
        "alert": "Low - Home Care"
    },
    "Typhoid": {
        "symptoms": ["fever", "weakness", "stomach pain", "headache"],
        "medicines": ["Antibiotics (Doctor prescribed)", "ORS"],
        "alert": "High - Doctor Required"
    }
}

# Prediction function
def predict_disease(symptoms):
    for disease, data in disease_data.items():
        match = any(symptom.lower() in data["symptoms"] for symptom in symptoms)
        if match:
            return disease, data["medicines"], data["alert"]
    return "Unknown", [], "Low - Home Care"

# User Input
st.write("Enter 2 or 3 symptoms separated by comma:")
user_input = st.text_input("Symptoms:", placeholder="fever, headache, cough")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter symptoms!")
    else:
        symptoms = [s.strip().lower() for s in user_input.split(",")]
        disease, medicines, alert = predict_disease(symptoms)

        st.success(f"🩺 Disease: {disease}")

        if medicines:
            st.markdown("### 💊 Suggested Medicines:")
            for med in medicines:
                st.write(f"- {med}")

        # Alert level color
        if "High" in alert:
            st.error(f"🚨 Alert Level: **{alert}**")
        else:
            st.warning(f"⚠️ Alert Level: **{alert}**")

st.markdown("<br><br><p style='color:red;'>🚑 This tool only gives suggestions. Always consult a doctor.</p>", unsafe_allow_html=True)
