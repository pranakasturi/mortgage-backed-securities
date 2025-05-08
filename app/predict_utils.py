import os
import joblib
import pandas as pd

MODEL_DIR = "models"

def load_models():
    models = {}
    model_files = {
        "logistic_regression": "logistic_regression_model.pkl",
        "xgboost": "xgboost_model.pkl",
        "lda": "lda_model.pkl",
        "gradient_boosting": "gradient_boosting_model.pkl"
    }
    for key, filename in model_files.items():
        path = os.path.join(MODEL_DIR, filename)
        if os.path.exists(path):
            models[key] = joblib.load(path)
        else:
            print(f"⚠️ Model not found: {path}")
    return models

models = load_models()

def make_prediction(model_key, features):
    model = models.get(model_key)
    if model is None:
        return {"error": f"Model '{model_key}' not found."}

    try:
        # Feature names must match what was used during training
        columns = ["CreditScore", "OCLTV", "DTI", "OrigUPB", "OrigInterestRate"]
        input_df = pd.DataFrame([features], columns=columns)

        prediction = model.predict(input_df)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        return {"error": f"Prediction failed: {e}"}
