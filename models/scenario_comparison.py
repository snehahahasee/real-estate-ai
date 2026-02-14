from models.risk_model import calculate_risk
from utils.rebuild_cashflow import rebuild_cashflow_from_record

def scenario_comparison(record):
    base_cashflow = rebuild_cashflow_from_record(record)

    results = {}

    # Optimistic
    modified = []
    for m in base_cashflow:
        temp = m.copy()
        temp["outflow"] *= 0.9
        temp["net"] = temp["inflow"] - temp["outflow"]
        temp["balance"] = temp["balance"] + temp["net"]
        modified.append(temp)

    risk, prob, _ = calculate_risk(modified)
    results["Optimistic"] = {"risk": risk, "probability": prob}

    # Base
    risk, prob, _ = calculate_risk(base_cashflow)
    results["Base"] = {"risk": risk, "probability": prob}

    # Pessimistic
    modified = []
    for m in base_cashflow:
        temp = m.copy()
        temp["outflow"] *= 1.2
        temp["net"] = temp["inflow"] - temp["outflow"]
        temp["balance"] = temp["balance"] + temp["net"]
        modified.append(temp)

    risk, prob, _ = calculate_risk(modified)
    results["Pessimistic"] = {"risk": risk, "probability": prob}

    return results
