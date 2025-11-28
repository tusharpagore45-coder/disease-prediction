import streamlit as st

st.set_page_config(page_title="Smart Disease Prediction System")

def predict_disease(symptoms):
    symptoms = [s.lower().strip() for s in symptoms]

    if "fever" in symptoms and "cough" in symptoms:
        return "Flu", 0.50
    if "headache" in symptoms and "vomiting" in symptoms:
        return "Migraine", 0.70
    if "chest pain" in symptoms or "breathing problem" in symptoms:
        return "Heart Attack (Suspected)", 0.95
    if "vomiting" in symptoms and "stomach pain" in symptoms:
        return "Food Poisoning", 0.60

    return "Common Cold", 0.20

medicine_db = {
    "Flu": ["Paracetamol 500mg", "Steam inhalation", "Rest well"],
    "Migraine": ["Painkiller", "Silent and dark place rest", "Hydration"],
    "Heart Attack (Suspected)": ["❗ Emergency - Go to Doctor Immediately"],
    "Food Poisoning": ["ORS", "Light food only", "Avoid oily food"],
    "Common Cold": ["Cetirizine 10mg", "Warm water", "Rest"]
}

st.title("🧠 Smart Disease Prediction System")
st.write("Enter symptoms separated by comma (,):")

input_text = st.text_input("Example: fever, cough")

if st.button("Predict"):
    if not input_text.strip():
        st.error("⚠ Please enter symptoms!")
    else:
        symptoms_list = [s.strip() for s in input_text.split(",")]

        disease, severity = predict_disease(symptoms_list)

        st.subheader("🩺 Predicted Disease")
        st.success(f"{disease}")
        st.write(f"Severity Score: {severity}")

        st.subheader("💊 Medicines / Care")
        for m in medicine_db.get(disease, ["Consult a doctor"]):
            st.write("• " + m)

        # Danger condition
        if severity >= 0.70 or "chest pain" in input_text.lower() or "breathing problem" in input_text.lower():
            st.error("🚨 DANGER: Go to Doctor Immediately!")
        else:
            st.info("🙂 Not a high risk. If symptoms increase, consult doctor.")

st.caption("⚠ This system gives suggestions only. Always consult a doctor.")
