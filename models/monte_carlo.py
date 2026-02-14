import random
from models.risk_model import calculate_risk
from utils.rebuild_cashflow import rebuild_cashflow_from_record

def monte_carlo_simulation(record, runs=200):
    probs = []

    for _ in range(runs):
        base_cashflow = rebuild_cashflow_from_record(record)
        modified = []

        for m in base_cashflow:
            temp = m.copy()
            temp["inflow"] *= random.uniform(0.85, 1.1)
            temp["outflow"] *= random.uniform(0.9, 1.2)
            temp["net"] = temp["inflow"] - temp["outflow"]
            temp["balance"] = temp["balance"] + temp["net"]
            modified.append(temp)

        _, prob, _ = calculate_risk(modified)
        probs.append(prob)

    return {
        "average": round(sum(probs) / len(probs), 2),
        "worst": max(probs),
        "best": min(probs)
    }
