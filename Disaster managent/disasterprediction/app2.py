from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend interaction

# Load trained model
model = None
model_path = "flood_model.pkl"

try:
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    print("⚠️ Model file not found! Please train and save a model as 'flood_model.pkl'.")

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array([
            float(data['AgriculturalPractices']),
            float(data['WetlandLoss']),
            float(data['DamsQuality']),
            float(data['InadequatePlanning']),
            float(data['ClimateChange'])
        ]).reshape(1, -1)

        if model:
            prediction = model.predict(features)[0]
            result = "🌊 High Flood Risk 🚨" if prediction >= 0.50 else "✅ Low Flood Risk"
        else:
            result = "❌ Model not available. Please train and save a model first."

        return jsonify({"prediction_text": result})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # Updated host & port