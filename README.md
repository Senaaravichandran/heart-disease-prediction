# 🫀 Cardiovra: Heart Disease Prediction

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

A state-of-the-art machine learning application that predicts the likelihood of heart disease based on patient medical data. Cardiovra features a highly optimized Naive Bayes predictive model wrapped in a beautiful, responsive, and glassmorphic user interface.

## ✨ Features

- **Accurate Predictions**: Powered by a trained Gaussian Naive Bayes model.
- **Premium UI/UX**: A stunning interface built with TailwindCSS, featuring animated gradients and glassmorphism.
- **Responsive Design**: Works flawlessly on both mobile devices and desktops.
- **Ready for Production**: Configured with Gunicorn and a Procfile for seamless deployment on platforms like Render or Heroku.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Senaaravichandran/heart-disease-prediction.git
   cd heart-disease-prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application locally**
   ```bash
   python app.py
   ```
   The app will be available at `http://127.0.0.1:5000/`.

## 🌐 Deployment (Render)

Deploying to Render is incredibly simple because the repository is already structured for it:

1. Create a new **Web Service** on Render.
2. Connect this GitHub repository.
3. Render will automatically detect the Python environment.
4. Set the **Build Command** to: `pip install -r requirements.txt`
5. Set the **Start Command** to: `gunicorn app:app` (or Render will detect the `Procfile`).

## 📊 Dataset & Model

- The model uses 11 clinical features (Age, Sex, Chest Pain Type, Resting BP, Cholesterol, etc.) to predict the presence of heart disease.
- The `model.pkl` is pre-trained and ready to infer based on the provided inputs.

---
*Built with ❤️ for better health diagnostics.*
