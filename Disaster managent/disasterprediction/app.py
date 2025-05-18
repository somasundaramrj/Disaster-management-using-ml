import numpy as np
import joblib
from flask import Flask, request, render_template

# Initialize Flask app
app = Flask(__name__)

# Load trained model and scaler
model = joblib.load("cyclone_model.pkl")
scaler = joblib.load("scaler.pkl")

# Home route - Display input form
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route - Handles user input
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get user input
        sea_temp = float(request.form["sea_temp"])
        humidity = float(request.form["humidity"])
        vorticity = float(request.form["vorticity"])
        pre_disturb = float(request.form["pre_disturb"])

        # Prepare and scale input data
        input_features = np.array([[sea_temp, humidity, vorticity, pre_disturb]])
        input_scaled = scaler.transform(input_features)

        # Make prediction
        prediction = model.predict(input_scaled)[0]
        result = "🌪️ CYCLONE DETECTED! ⚠️" if prediction == 1 else "🚫 NO CYCLONE"

        return render_template("index.html", prediction_result=result)

    except Exception as e:
        return render_template("index.html", prediction_result=f"Error: {str(e)}")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
