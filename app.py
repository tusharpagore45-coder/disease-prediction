def predict_disease(symptoms):
    symptoms = [s.lower().strip() for s in symptoms]

    # Dengue
    if "fever" in symptoms and "headache" in symptoms and "joint pain" in symptoms:
        return "Dengue (Suspected)", 0.85
    
    # Malaria
    if "fever" in symptoms and "chills" in symptoms:
        return "Malaria (Suspected)", 0.80
    
    # Typhoid
    if "fever" in symptoms and "stomach pain" in symptoms:
        return "Typhoid (Suspected)", 0.75
    
    # Flu / Viral Infection
    if "fever" in symptoms and "cough" in symptoms:
        return "Flu / Viral Infection", 0.50
    
    # Migraine
    if "headache" in symptoms and "vomiting" in symptoms:
        return "Migraine", 0.70
    
    # Asthma
    if "breathing problem" in symptoms and "chest tight" in symptoms:
        return "Asthma (Suspected)", 0.90

    # Heart Attack
    if "chest pain" in symptoms:
        return "Heart Attack (Suspected)", 0.95

    # Food Poisoning
    if "vomiting" in symptoms and "stomach pain" in symptoms:
        return "Food Poisoning", 0.60
    
    # COVID-like
    if "fever" in symptoms and "body pain" in symptoms and "cough" in symptoms:
        return "Covid-like Infection", 0.65

    return "Common Cold", 0.20
