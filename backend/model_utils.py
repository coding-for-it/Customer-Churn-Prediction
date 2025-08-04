import pandas as pd
import joblib
import os
import pickle

# Load model
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "models", "random_forest_model.pkl")
    return joblib.load(model_path)

# Preprocess input using saved columns
def preprocess_input(input_df):
    columns_path = os.path.join(os.path.dirname(__file__), "models", "columns_used.pkl")

    with open(columns_path, "rb") as f:
        trained_columns = pickle.load(f)

    # One-hot encode user input
    input_encoded = pd.get_dummies(input_df)

    # Add missing columns
    for col in trained_columns:
        if col not in input_encoded:
            input_encoded[col] = 0

    # Reorder to match training set
    input_encoded = input_encoded[trained_columns]

    return input_encoded

# Predict churn
def predict_churn(model, input_df):
    prediction = model.predict(input_df)[0]
    return "Yes" if prediction == 1 else "No"
