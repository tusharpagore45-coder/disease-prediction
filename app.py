import streamlit as st

st.set_page_config(page_title="Smart Disease Prediction System", page_icon="🧠", layout="wide")

# Disease database
DISEASE_DB = {
    ("fever", "cough", "cold"): ("Flu", ["Paracetamol", "Cough Syrup", "Drink warm water"], "Medium"),
    ("fever", "headache", "body pain"): ("Dengue", ["Paracetamol", "ORS", "Platelet monitoring"], "High - Doctor Required"),
    ("chest pain", "breathlessness"): ("Heart Attack (Emergency)", ["Aspirin", "Call ambulance"], "Very High - Immediate Hospital"),
    ("vomiting", "stomach pain"): ("Food Poisoning", ["ORS", "Antibiotic", "Hydration"], "Low"),
    ("fever", "rash", "joint pain"): ("Chikungunya", ["Painkillers", "Rest"], "Medium"),
    ("sneezing", "itchy eyes"): ("Allergy", ["Antihistamine", "Avoid dust"], "Low"),
    ("loose motion", "vomiting"): ("Diarrhea", ["ORS", "Zinc tablets"], "Medium"),
    ("headache", "vomiting", "high fever"): ("Meningitis", ["Hospitalization required"], "High - Doctor Required"),
    ("weight loss", "night sweats", "cough"): ("TB", ["TB Test", "Doctor Consultation"], "High"),
}

def predict_disease(input_symptoms):
    symptoms = [s.lower().strip() for s in input_symptoms.split(",")]

    for key, value in DISEASE_DB.items():
        if all(symptom in symptoms for symptom in key):
            return value
        
    return ("Common Cold", ["Rest", "Steam inhalation"], "Low")

# UI
st.markdown("<h1 style='color:yellow;'>🧠 Smart Disease Prediction System</h1>", unsafe_allow_html=True)
st.write("Enter 2 or 3 symptoms separated by comma: (Example: fever, cough, cold)")
user_input = st.text_input("Symptoms")

if st.button("Predict"):
    if user_input:
        disease, medicine, alert = predict_disease(user_input)
        st.success(f"🩺 Disease: **{disease}**")
        st.warning(f"💊 Suggested Medicines:\n- " + "\n- ".join(medicine))
        st.info(f"⚠️ Alert Level: **{alert}**")
    else:
        st.error("Please enter symptoms!")

st.caption("🚨 This tool only gives suggestions. Always consult a doctor.")
