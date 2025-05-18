import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load trained model
model = pickle.load(open("earthquake_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index3.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Debug: Print incoming data
        print("Received data:", data)

        # Extract features
        latitude = float(data["latitude"])
        longitude = float(data["longitude"])
        depth = float(data["depth"])

        features = np.array([latitude, longitude, depth]).reshape(1, -1)

        # Predict
        prediction = model.predict(features)[0]

        # Generate response
        if prediction > 6.0:
            result = f"🚨 High Risk of Earthquake (Magnitude: {prediction:.2f})"
        else:
            result = f"✅ Low Risk of Earthquake (Magnitude: {prediction:.2f})"

        # Debug: Print prediction result
        print("Prediction:", result)

        return jsonify({"prediction_text": result})
    
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000, debug=True) 
