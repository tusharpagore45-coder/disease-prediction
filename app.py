import streamlit as st

# Basic page settings
st.set_page_config(page_title="Smart Disease Predictor", page_icon="🧠", layout="centered")

# Title
st.title("🧠 Smart Disease Prediction System")

# Instruction
st.write("Enter symptoms separated by commas (,) e.g. fever, cough")

# Input box
symptoms_input = st.text_input("Symptoms:")

# Button
if st.button("Predict"):
    if symptoms_input.strip() == "":
        st.error("⚠️ Please enter at least one symptom!")
    else:
        st.success("🩺 Disease prediction will be shown here.")
        st.info("This is only for educational purpose. Always consult a doctor.")
