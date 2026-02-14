from models.risk_model import calculate_risk
from utils.rebuild_cashflow import rebuild_cashflow_from_record

def sensitivity_analysis(record):
    base_cashflow = rebuild_cashflow_from_record(record)

    results = {}

    # ---- Revenue Sensitivity (-10%) ----
    modified = []
    for m in base_cashflow:
        temp = m.copy()
        temp["inflow"] *= 0.9
        temp["net"] = temp["inflow"] - temp["outflow"]
        temp["balance"] = temp["balance"] + temp["net"]
        modified.append(temp)

    _, prob, _ = calculate_risk(modified)
    results["Revenue -10%"] = {
        "probability": prob
    }

    # ---- Cost Sensitivity (+10%) ----
    modified = []
    for m in base_cashflow:
        temp = m.copy()
        temp["outflow"] *= 1.1
        temp["net"] = temp["inflow"] - temp["outflow"]
        temp["balance"] = temp["balance"] + temp["net"]
        modified.append(temp)

    _, prob, _ = calculate_risk(modified)
    results["Cost +10%"] = {
        "probability": prob
    }

    return results
