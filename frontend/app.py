import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.model_utils import load_model, preprocess_input, predict_churn

st.title("🔁 Customer Churn Prediction")
st.markdown("Check if a customer is likely to leave your service.")

st.subheader("📋 Enter Customer Info")

# Collect inputs (keep it simple)
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["Yes", "No"])
partner = st.selectbox("Has Partner?", ["Yes", "No"])
dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total = st.number_input("Total Charges", 0.0, 10000.0, 1500.0)

# Predict button
if st.button("Predict Churn"):
    input_df = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "InternetService": internet_service,
        "TechSupport": tech_support,
        "Contract": contract,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }])

    model = load_model()
    processed = preprocess_input(input_df)
    result = predict_churn(model, processed)

    st.success(f"Will the customer churn? **{result}**")
