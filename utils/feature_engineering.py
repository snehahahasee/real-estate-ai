import numpy as np

def extract_features(cashflow):
    balances = np.array([m["balance"] for m in cashflow])
    inflows = np.array([m["inflow"] for m in cashflow])
    outflows = np.array([m["outflow"] for m in cashflow])

    initial_balance = balances[0]
    final_balance = balances[-1]
    min_balance = balances.min()

    avg_inflow = inflows.mean()
    avg_outflow = outflows.mean()

    # ---- Engineered Features ----
    burn_ratio = avg_outflow / avg_inflow if avg_inflow != 0 else 2
    trend_ratio = (final_balance - initial_balance) / initial_balance
    buffer_ratio = min_balance / initial_balance

    return np.array([[burn_ratio, trend_ratio, buffer_ratio]])
