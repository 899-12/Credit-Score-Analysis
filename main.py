# Import all files
from feature import get_features
from utils import generate_credit_score
from train_model import train_model
import joblib
import pandas as pd

if __name__ == "__main__":
    json_path = "D:/2-OpenAI Chatbot/ZERU/user-wallet-transactions.json"
    # Calling get_features to perform feature extraction 
    features_df = get_features(json_path)
    # Generate credit score
    features_df['credit_score'] = features_df.apply(generate_credit_score, axis=1)

    # Train model is called to train the model defined in the model.py
    model = train_model(features_df)

    # Load model again to score
    model = joblib.load("D:/2-OpenAI Chatbot/ZERU/model.pkl")
    X = features_df.drop(columns=['userWallet', 'credit_score'])
    features_df['predicted_score'] = model.predict(X)
    import matplotlib.pyplot as plt

    features_df['predicted_score'].hist(bins=10, range=(0, 1000))
    plt.title("Score Distribution")
    plt.xlabel("Score Range")
    plt.ylabel("Number of Wallets")
    plt.savefig("score_distribution.png")

    # Storing the predicted score to score_output.csv
    features_df[['userWallet', 'predicted_score']].to_csv("score_output.csv", index=False)
    print("✅ Credit scores generated in score_output.csv")
