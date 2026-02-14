def apply_scenario(cashflow, delay_months, cost_increase, revenue_drop):
    updated = []
    balance = cashflow[0]["balance"]

    for i, row in enumerate(cashflow):
        inflow = row["inflow"]
        outflow = row["outflow"]

        # Delay: no inflow during delay months
        if i < delay_months:
            inflow = 0

        # Apply revenue drop
        inflow = inflow * (1 - revenue_drop / 100)

        # Apply cost inflation
        outflow = outflow * (1 + cost_increase / 100)

        net = inflow - outflow
        balance += net

        updated.append({
            "month": row["month"],
            "inflow": round(inflow, 2),
            "outflow": round(outflow, 2),
            "net": round(net, 2),
            "balance": round(balance, 2)
        })

    return updated
