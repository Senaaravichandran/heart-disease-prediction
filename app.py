import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
import logging

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

@app.route('/predict', methods=['POST'])
def predict():
    """Handles prediction requests from the frontend."""
    if not model:
        return render_template('index.html', prediction_text="Error: Model not loaded. Please check server logs.")
        
    try:
        # Extract features from form input
        input_data = [
            float(request.form['Age']),
            int(request.form['Sex']),
            int(request.form['ChestPainType']),
            float(request.form['RestingBP']),
            float(request.form['Cholesterol']),
            int(request.form['FastingBS']),
            int(request.form['RestingECG']),
            float(request.form['MaxHR']),
            int(request.form['ExerciseAngina']),
            float(request.form['Oldpeak']),
            int(request.form['ST_Slope']),
        ]
        
        # Convert to numpy array for prediction
        features = np.array([input_data])
        prediction = model.predict(features)[0]

        # Format result based on prediction
        if prediction == 1:
            result = "The patient shows indicators of heart disease. Please consult a cardiologist immediately for a full evaluation."
        else:
            result = "No significant indicators of heart disease detected. Keep maintaining a healthy lifestyle!"
            
        return render_template('index.html', prediction_text=result)

    except ValueError as ve:
        logger.error(f"Validation Error: {ve}")
        return render_template('index.html', prediction_text="Error: Invalid input data. Please ensure all fields are correctly filled.")
    except Exception as e:
        logger.error(f"Prediction Error: {e}")
        return render_template('index.html', prediction_text="An unexpected error occurred while processing your request.")

if __name__ == "__main__":
    app.run(debug=True)
