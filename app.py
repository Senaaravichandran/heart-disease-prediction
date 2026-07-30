import numpy as np
import pandas as pd
from flask import Flask, request, render_template, jsonify
import pickle
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load the trained model
try:
    model = pickle.load(open('model.pkl', 'rb'))
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    model = None

@app.route('/')
def home():
    """Renders the main prediction page."""
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    """Handles JSON prediction requests from the frontend."""
    if not model:
        return jsonify({"status": "error", "message": "Model not loaded. Please check server logs."}), 500
        
    try:
        data = request.json
        
        # Add a small delay for UI effect (optional, makes it feel like it's "calculating")
        time.sleep(1.5)
        
        # Extract features from JSON input
        input_data = [
            float(data.get('Age', 0)),
            int(data.get('Sex', 0)),
            int(data.get('ChestPainType', 0)),
            float(data.get('RestingBP', 0)),
            float(data.get('Cholesterol', 0)),
            int(data.get('FastingBS', 0)),
            int(data.get('RestingECG', 0)),
            float(data.get('MaxHR', 0)),
            int(data.get('ExerciseAngina', 0)),
            float(data.get('Oldpeak', 0)),
            int(data.get('ST_Slope', 0)),
        ]
        
        # Convert to numpy array for prediction
        features = np.array([input_data])
        prediction = int(model.predict(features)[0])

        # Format result based on prediction
        if prediction == 1:
            result = "The patient shows indicators of heart disease. Please consult a cardiologist immediately for a full evaluation."
            status = "high_risk"
        else:
            result = "No significant indicators of heart disease detected. Keep maintaining a healthy lifestyle!"
            status = "normal"
            
        return jsonify({
            "status": status,
            "message": result,
            "prediction": prediction
        })

    except ValueError as ve:
        logger.error(f"Validation Error: {ve}")
        return jsonify({"status": "error", "message": "Invalid input data. Please ensure all fields are numeric."}), 400
    except Exception as e:
        logger.error(f"Prediction Error: {e}")
        return jsonify({"status": "error", "message": "An unexpected error occurred while processing your request."}), 500

if __name__ == "__main__":
    app.run(debug=True)
