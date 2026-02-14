from models.risk_model import calculate_risk
from utils.rebuild_cashflow import rebuild_cashflow_from_record

def compute_feature_importance(record):
    base_cashflow = rebuild_cashflow_from_record(record)
    _, base_prob, _ = calculate_risk(base_cashflow)

    features = {}

    # Revenue impact
    modified = []
    for m in base_cashflow:
        temp = m.copy()
        temp["inflow"] *= 0.9
        temp["net"] = temp["inflow"] - temp["outflow"]
        temp["balance"] += temp["net"]
        modified.append(temp)

    _, prob, _ = calculate_risk(modified)
    features["Revenue"] = abs(base_prob - prob)

    # Cost impact
    modified = []
    for m in base_cashflow:
        temp = m.copy()
        temp["outflow"] *= 1.1
        temp["net"] = temp["inflow"] - temp["outflow"]
        temp["balance"] += temp["net"]
        modified.append(temp)

    _, prob, _ = calculate_risk(modified)
    features["Cost"] = abs(base_prob - prob)

    # Delay impact (simplified proxy)
    features["Delay"] = record.delay * 2

    # Inflation impact
    features["Inflation"] = record.inflation * 1.5

    return features
