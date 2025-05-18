import google.generativeai as genai
import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Set API key directly here (Replace with your actual API key)
genai.configure(api_key="AIzaSyBqvNrLJpMws4x7YyPr0ahq1_mQAQQ4IQU")

model = genai.GenerativeModel("gemini-1.5-pro-latest")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message", "").strip()
        if not user_input:
            return jsonify({"response": "Please enter a valid question."})

        response = model.generate_content(user_input)
        ai_response = response.text if response.text else "No response from AI."

        return jsonify({"response": ai_response})

    except Exception as e:
        print(f"❌ Error: {str(e)}")  # Debugging
        return jsonify({"response": f"Error: {str(e)}"}), 500

# ✅ Corrected entry point
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True) 
