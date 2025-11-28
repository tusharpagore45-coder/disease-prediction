<!DOCTYPE html>
<html>
<head>
    <title>Smart Disease Prediction System</title>
    <style>
        body {
            font-family: Arial;
            margin: 40px;
            background: #f5f5f5;
        }
        .box {
            background: white;
            padding: 20px;
            border-radius: 8px;
            width: 400px;
        }
        button {
            padding: 10px;
            background: green;
            color: white;
            border-radius: 5px;
            cursor: pointer;
            border: none;
            width: 100%;
        }
        #result {
            margin-top: 20px;
            padding: 15px;
            background: #e8ffe8;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<h2>Smart Disease Prediction System</h2>

<div class="box">
    <label>Enter Symptoms:</label><br><br>
    <input id="symptoms" type="text" placeholder="Example: fever, cough" style="width:100%; padding:10px;"><br><br>

    <button onclick="predict()">Predict Disease</button>

    <div id="result"></div>
</div>

<script>

function predict() {
    let s = document.getElementById("symptoms").value.toLowerCase();
    let disease = "";
    let medicine = "";
    let danger = "";

    // Simple rule based prediction
    if (s.includes("fever") && s.includes("cough")) {
        disease = "Flu / Viral Infection";
        medicine = "Paracetamol, Cough Syrup, Rest";
        danger = "Low Risk";
    }
    else if (s.includes("headache") && s.includes("vomiting")) {
        disease = "Migraine";
        medicine = "Pain Killer, Hydration, Rest";
        danger = "Medium Risk";
    }
    else if (s.includes("chest pain") || s.includes("breathing problem")) {
        disease = "Possible Heart / Lung Issue";
        medicine = "No self-medication";
        danger = "High Risk — Visit Doctor Immediately";
    }
    else {
        disease = "Unknown — Symptoms not found";
        medicine = "Consult Doctor";
        danger = "Check properly";
    }

    document.getElementById("result").innerHTML = `
        <b>Disease Prediction:</b> ${disease}<br><br>
        <b>Suggested Medicine:</b> ${medicine}<br><br>
        <b>Danger Level:</b> ${danger}
    `;
}

</script>

</body>
</html>
