import streamlit as st
import pickle
import pandas as pd

#Load both model and column names
with open("random_forest_model.pkl", "rb") as file:
    model, model_columns = pickle.load(file)

#App title
st.title("Customer Churn Prediction")

#Step 1: Collect simple user inputs
gender = st.selectbox("Gender", ["Female", "Male"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

#Step 2: Build input dictionary
input_dict = {
    "tenure": tenure,
    "MonthlyCharges": monthly_charges,
    "gender_Male": 1 if gender == "Male" else 0,
    "InternetService_Fiber optic": 1 if internet == "Fiber optic" else 0,
    "InternetService_No": 1 if internet == "No" else 0,
    "Contract_One year": 1 if contract == "One year" else 0,
    "Contract_Two year": 1 if contract == "Two year" else 0
}

#Convert to DataFrame
input_df = pd.DataFrame([input_dict])

#Match with model columns
for col in model_columns:
    if col not in input_df.columns:
        input_df[col] = 0

#Sort columns
input_df = input_df[model_columns]

#Step 5: Predict on button click
if st.button("Predict Churn"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("This customer is likely to CHURN.")
    else:
        st.success("This customer is NOT likely to churn.")
