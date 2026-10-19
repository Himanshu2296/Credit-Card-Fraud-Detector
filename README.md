# Credit Card Fraud Detector

## Overview
A machine learning project that identifies potentially fraudulent credit card transactions using the publicly available Credit Card Fraud Detection dataset.

## Objectives
- Explore and understand transaction data.
- Analyze severe class imbalance.
- Train a Logistic Regression baseline.
- Compare Logistic Regression with Random Forest.
- Evaluate the selected model using fraud-focused metrics.
- Build a terminal-based prediction demonstration.

## Models
- Logistic Regression
- Random Forest

## Evaluation
Models are compared using fraud precision, recall, F1-score, Average Precision, and the confusion matrix.

## Dataset
The dataset contains 284,807 transactions and 31 columns, including the `Class` target column.

- `0`: Legitimate transaction
- `1`: Fraudulent transaction

Dataset source: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

## Technologies
Python, pandas, NumPy, scikit-learn, joblib, and Jupyter Notebook.

## How to Run
1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Download the dataset from Kaggle.
5. Place `creditcard.csv` inside the `data/` directory.
6. Open `Credit_Card_Fraud_Detector.ipynb` in Jupyter Notebook and run the cells in order.

## Limitations
Predictions are estimates and should not be treated as definitive proof of fraud. The dataset's PCA-transformed features are not directly interpretable as ordinary transaction details. This project is an educational demonstration, not a production payment-security system.

## Streamlit Web Application

The project includes a Streamlit interface for testing the trained fraud-detection model.

### Run locally

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Download the dataset from the source listed above and place it in the `data/` directory.
5. Run the notebook cells in order to train and save `fraud_model.joblib`.
6. Start the application:

   ```bash
   python -m streamlit run app.py
   ```

### Limitations

The model expects 30 numerical features, including PCA-transformed features `V1`–`V28`. The application is an educational demonstration, not a production payment-security system. Its predictions are estimates, not definitive proof of fraud.
