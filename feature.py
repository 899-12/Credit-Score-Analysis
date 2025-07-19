
import pandas as pd
import numpy as np

# Loads the json data using read_json
def load_data(json_path):
    df = pd.read_json(json_path)
    return df

# Define the function to preprocess the data
def preprocess(df):
    # USD value of each column is calculated by multiplying amount and assetPrice
    df['usd_value'] = df['actionData'].apply(lambda x: float(x['amount']) * float(x['assetPriceUSD']) if x else 0)
    df['usd_value'] = df.apply(lambda x: x['usd_value'] / 1e6 if x['actionData']['assetSymbol'] == "USDC" else x['usd_value'] / 1e18, axis=1)
    return df


def get_features(json_path):
    df = load_data(json_path)
    df = preprocess(df)

    feature_df = df.groupby('userWallet').apply(lambda x: pd.Series({
        # Total number of transactions
        'num_txns': x.shape[0],
        # number of deposits
        'num_deposits': (x['action'] == 'deposit').sum(),
        # Number of borrows
        'num_borrows': (x['action'] == 'borrow').sum(),
        # Repayments
        'num_repays': (x['action'] == 'repay').sum(),
        'num_liquidations': (x['action'] == 'liquidationcall').sum(),
        # Total deposit
        'total_deposit_usd': x[x['action'] == 'deposit']['usd_value'].sum(),
        # Total borrows
        'total_borrow_usd': x[x['action'] == 'borrow']['usd_value'].sum(),
        # Total repay value
        'total_repay_usd': x[x['action'] == 'repay']['usd_value'].sum()
    })).reset_index()
    # Borrowed values repaid
    feature_df['borrow_repay_ratio'] = feature_df.apply(
        lambda row: row['total_repay_usd'] / row['total_borrow_usd'] if row['total_borrow_usd'] > 0 else 0,
        axis=1
    )
    feature_df['has_liquidation'] = (feature_df['num_liquidations'] > 0).astype(int)

    return feature_df
