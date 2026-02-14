def predict_future(cashflow, months=6):
    balances = [m["balance"] for m in cashflow]

    if len(balances) < 2:
        return balances

    trend = balances[-1] - balances[-2]
    future = []

    last = balances[-1]
    for _ in range(months):
        last += trend
        future.append(round(last, 2))

    return future
