# Credit-Score-Analysis


## 📌 Objective
This project builds a machine learning model to assign a **credit score (0–1000)** to each wallet based on historical transaction-level data from the Aave V2 protocol. The scores reflect responsible DeFi behavior such as regular repayments, deposits, and avoiding liquidation.

## ⚙️ Architecture Overview

Feature Engineering → Credit Score Generation → ML Model Training & Prediction


## 🧠 Scoring Logic

- **Base score:** 300
- +10 points per deposit
- +0.005 × total deposit value (USD)
- +15 points per repayment
- −100 points per liquidation
- +up to 100 points based on repay-to-borrow ratio
- Score is clipped to the 0–1000 range

## 📂 Project Structure

| File              | Description |
|------------------|-------------|
| `main.py`         | Orchestrates the pipeline from JSON to final scores |
| `feature.py`      | Preprocessing and feature extraction |
| `utils.py`        | Credit score generation logic |
| `train_model.py`  | Model training, evaluation, and persistence |
| `score_output.csv`| Predicted credit scores |
| `score_distribution.png` | Score histogram |
| `analysis.md`     | Behavioral analysis of scored wallets |

## 🚀 Run Instructions

1. Set your input JSON path in `main.py`
2. Run the main script:

```bash
python main.py

```
📦 Requirements

```
pip install pandas numpy scikit-learn matplotlib joblib
```

