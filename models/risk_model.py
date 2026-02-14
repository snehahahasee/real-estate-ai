import numpy as np
from sklearn.linear_model import LogisticRegression
from utils.feature_engineering import extract_features

# -------- TRAIN ML MODEL (SYNTHETIC DATA) --------
X_train = np.array([
    [0.6, 0.2, 0.9],
    [0.8, 0.1, 0.7],
    [1.0, 0.0, 0.5],
    [1.2, -0.1, 0.4],
    [1.4, -0.2, 0.2],
    [1.6, -0.3, 0.1]
])

y_train = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X_train, y_train)

FEATURE_NAMES = ["Burn Ratio", "Cash Trend", "Liquidity Buffer"]

def calculate_risk(cashflow):
    features = extract_features(cashflow)

    prob = model.predict_proba(features)[0][1]
    probability = int(prob * 100)

    if probability < 30:
        risk = "🟢 Low Risk"
    elif probability < 60:
        risk = "🟡 Medium Risk"
    else:
        risk = "🔴 High Risk"

    importance = dict(zip(FEATURE_NAMES, model.coef_[0]))

    return risk, probability, importance
