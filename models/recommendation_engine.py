def investment_recommendation(probability):
    if probability < 25:
        return "✅ Proceed with Investment", "Low risk with healthy cash-flow indicators."
    elif probability < 50:
        return "⚠️ Proceed with Caution", "Moderate risk. Consider renegotiating costs or timelines."
    else:
        return "❌ Avoid Investment", "High probability of failure under current conditions."
