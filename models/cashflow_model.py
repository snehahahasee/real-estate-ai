def calculate_cashflow(inputs, months=12):
    loan_amount = float(inputs["loan_amount"])
    interest_rate = float(inputs["interest_rate"]) / 100
    monthly_revenue = float(inputs["monthly_revenue"])
    monthly_cost = float(inputs["monthly_cost"])

    monthly_interest = (loan_amount * interest_rate) / 12

    cashflow = []
    balance = loan_amount

    for month in range(1, months + 1):
        inflow = monthly_revenue
        outflow = monthly_cost + monthly_interest
        net = inflow - outflow
        balance += net

        cashflow.append({
            "month": month,
            "inflow": inflow,
            "outflow": outflow,
            "net": net,
            "balance": balance
        })

    return cashflow
