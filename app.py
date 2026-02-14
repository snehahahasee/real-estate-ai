from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from models.database import db, User, Analysis
from models.cashflow_model import calculate_cashflow
from models.risk_model import calculate_risk
from utils.scenario_simulator import apply_scenario

from models.feature_importance import compute_feature_importance

from models.sensitivity_analysis import sensitivity_analysis
from models.monte_carlo import monte_carlo_simulation
from models.scenario_comparison import scenario_comparison
from models.recommendation_engine import investment_recommendation

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# ---------- HOME ----------
@app.route("/")
def home():
    return render_template("index.html")

# ---------- AUTH ----------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            password=generate_password_hash(request.form["password"]),
            role=request.form["role"]
        )
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and check_password_hash(user.password, request.form["password"]):
            session.clear()
            session["user_id"] = user.id
            session["role"] = user.role
            return redirect("/input")
        return "Invalid credentials"
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ---------- INPUT ----------
@app.route("/input", methods=["GET", "POST"])
def input_page():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        data = request.form.to_dict()

        base = calculate_cashflow(data)
        scenario = apply_scenario(
            base,
            int(data["delay"]),
            float(data["cost_increase"]),
            float(data["revenue_drop"])
        )

        risk, probability, _ = calculate_risk(scenario)

        record = Analysis(
            user_id=session["user_id"],
            loan_amount=float(data["loan_amount"]),
            interest_rate=float(data["interest_rate"]),
            revenue=float(data["monthly_revenue"]),
            cost=float(data["monthly_cost"]),
            delay=int(data["delay"]),
            inflation=float(data["cost_increase"]),
            revenue_drop=float(data["revenue_drop"]),
            risk=risk,
            probability=probability
        )
        db.session.add(record)
        db.session.commit()

        # 🔑 STORE ONLY ID
        session["last_analysis_id"] = record.id

        return redirect("/dashboard")

    return render_template("input.html")

# ---------- DASHBOARD ----------
@app.route("/dashboard")
def dashboard():
    if "last_analysis_id" not in session:
        return redirect("/input")

    record = Analysis.query.get(session["last_analysis_id"])

    inputs = {
        "loan_amount": record.loan_amount,
        "interest_rate": record.interest_rate,
        "monthly_revenue": record.revenue,
        "monthly_cost": record.cost
    }

    base = calculate_cashflow(inputs)
    scenario = apply_scenario(
        base,
        record.delay,
        record.inflation,
        record.revenue_drop
    )

    risk, probability, _ = calculate_risk(scenario)

    return render_template(
        "dashboard.html",
        cashflow=scenario,
        risk=risk,
        probability=probability
    )

# ---------- ADVANCED MODULES ----------
@app.route("/sensitivity")
def sensitivity():
    record = Analysis.query.get(session.get("last_analysis_id"))
    result = sensitivity_analysis(record)
    return render_template("sensitivity.html", result=result)

@app.route("/monte-carlo")
def monte_carlo():
    record = Analysis.query.get(session.get("last_analysis_id"))
    result = monte_carlo_simulation(record)
    return render_template("monte_carlo.html", result=result)

@app.route("/scenarios")
def scenarios():
    record = Analysis.query.get(session.get("last_analysis_id"))
    result = scenario_comparison(record)
    return render_template("scenarios.html", result=result)

@app.route("/recommendation")
def recommendation():
    record = Analysis.query.get(session.get("last_analysis_id"))
    title, explanation = investment_recommendation(record.probability)
    return render_template(
        "recommendation.html",
        title=title,
        explanation=explanation,
        probability=record.probability
    )

# ---------- HISTORY ----------
@app.route("/history")
def history():
    if "user_id" not in session:
        return redirect("/login")

    records = Analysis.query.filter_by(
        user_id=session["user_id"]
    ).order_by(Analysis.timestamp.desc()).all()

    return render_template("history.html", records=records)


@app.route("/history/view/<int:analysis_id>")
def view_history_analysis(analysis_id):
    if "user_id" not in session:
        return redirect("/login")

    record = Analysis.query.get_or_404(analysis_id)

    # Security check
    if record.user_id != session["user_id"]:
        return "Unauthorized"

    # 🔑 Set session to selected analysis
    session["last_analysis_id"] = record.id

    return redirect("/dashboard")
@app.route("/feature-importance")
def feature_importance():
    record = Analysis.query.get(session.get("last_analysis_id"))
    result = compute_feature_importance(record)
    return render_template("feature_importance.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
