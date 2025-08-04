# 📉 Customer Churn Prediction

A machine learning solution to predict if a customer is likely to churn based on behavior and account features.

## 🚀 Tech Stack
- Python
- Pandas, NumPy, Scikit-learn
- Matplotlib, Seaborn
- Streamlit
- Docker

## 📁 Project Structure
Customer-Churn-Prediction-main/
│
├── churn_pipeline.ipynb # EDA + model training
├── app.py # Streamlit app
├── customer_churn.csv # Dataset
├── logistic_model.pkl # Saved model
├── requirements.txt # Python dependencies
├── Dockerfile # Containerization
└── README.md # Project overview


## 🧪 Models Used
- Logistic Regression
- Random Forest

## 🎯 Evaluation Metrics
- Accuracy
- Precision, Recall, F1-Score
- ROC-AUC Curve

<<<<<<< HEAD
## 🖥 Deployment
Run the app locally:
=======
- Python 
- Pandas, NumPy for data manipulation
- Seaborn, Matplotlib for visualization
- Scikit-learn for ML models
- Streamlit for frontend UI
- Docker for containerized deployment
>>>>>>> 1c4dc39e972817fd9fba49c9adda77efc02d634a

```bash
streamlit run app.py
```

Or build the Docker container:

```bash
docker build -t churn-app .
docker run -p 8501:8501 churn-app
```
