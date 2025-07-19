
import numpy as np

def generate_credit_score(row):
    score = 300
    score += row['num_deposits'] * 10
    score += row['total_deposit_usd'] * 0.005
    score += row['num_repays'] * 15
    score -= row['num_liquidations'] * 100
    if row['total_borrow_usd'] > 0:
        repay_ratio = row['total_repay_usd'] / row['total_borrow_usd']
        score += min(repay_ratio, 1.0) * 100
    return np.clip(score, 0, 1000)
