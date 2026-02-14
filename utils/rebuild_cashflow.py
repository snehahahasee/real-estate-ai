from models.cashflow_model import calculate_cashflow
from utils.scenario_simulator import apply_scenario

def rebuild_cashflow_from_record(record):
    base_inputs = {
        "loan_amount": record.loan_amount,
        "interest_rate": record.interest_rate,
        "monthly_revenue": record.revenue,
        "monthly_cost": record.cost
    }

    base = calculate_cashflow(base_inputs)

    scenario = apply_scenario(
        base,
        record.delay,
        record.inflation,
        record.revenue_drop
    )

    return scenario
