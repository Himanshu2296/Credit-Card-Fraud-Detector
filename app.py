
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Credit Card Fraud Detector",
    layout="centered"
)

st.title("Credit Card Fraud Detector")
st.write("Enter the transaction features to estimate its fraud risk.")

MODEL_PATH = Path(__file__).parent / "fraud_model.joblib"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

if not MODEL_PATH.exists():
    st.error(
        "Model file not found. Save fraud_model.joblib "
        "from your completed Jupyter Notebook first."
    )
    st.stop()

model = load_model()

feature_names = ["Time"] + [f"V{i}" for i in range(1, 29)] + ["Amount"]

with st.form("transaction_form"):
    st.subheader("Transaction features")

    values = {}

    for feature in feature_names:
        if feature == "Time":
            values[feature] = st.number_input(
                feature, min_value=0.0, value=0.0
            )
        elif feature == "Amount":
            values[feature] = st.number_input(
                feature, min_value=0.0, value=1.0
            )
        else:
            values[feature] = st.number_input(
                feature, value=0.0, format="%.6f"
            )

    submitted = st.form_submit_button("Predict transaction")

if submitted:
    transaction = pd.DataFrame([values], columns=feature_names)

    prediction = model.predict(transaction)[0]
    probability = model.predict_proba(transaction)[0][1]

    st.subheader("Prediction result")
    st.metric("Estimated fraud probability", f"{probability:.2%}")

    if prediction == 1:
        st.error("Potentially fraudulent transaction")
    else:
        st.success("Likely legitimate transaction")

st.caption(
    "Educational demonstration only. Predictions are estimates, "
    "not definitive proof of fraud."
)
