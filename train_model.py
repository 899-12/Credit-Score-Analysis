# aave-defi-credit-score/src/train_model.py
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def train_model(features_df, model_path="D:/2-OpenAI Chatbot/ZERU/model.pkl"):
    X = features_df.drop(columns=['userWallet', 'credit_score'])
    y = features_df['credit_score']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("MAE:", mean_absolute_error(y_test, y_pred))
    print("R² Score:", model.score(X_test, y_test))

    joblib.dump(model, model_path)
    return model
