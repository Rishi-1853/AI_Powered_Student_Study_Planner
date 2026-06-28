from flask import Flask, render_template, request, redirect, url_for
import joblib
import sys
from Database.db_utils import (
    register_user,
    login_user,
    save_history,
    get_history
)
from flask import session
from planner.planner_utils import create_study_plan
sys.path.append("database")
from AI.ai_recommendation import analyze_student
from Database.db_utils import (
    save_history,
    get_history
)
app = Flask(__name__)

app.secret_key = "study_planner_secret"

# ==========================================
# LOAD MODELS
# ==========================================

try:
    performance_model = joblib.load(
        "models/performance_model.pkl"
    )

    priority_model = joblib.load(
        "models/priority_model.pkl"
    )

    model_columns = joblib.load(
        "models/model_columns.pkl"
    )

    priority_columns = joblib.load(
        "models/priority_columns.pkl"
    )

    print("Models Loaded Successfully")

except Exception as e:

    print("Error Loading Models:")
    print(e)



def get_recommendations(predicted_score):

    recommendations = []

    if predicted_score < 60:
        recommendations.append(
            "Increase study hours"
        )

    if predicted_score < 75:
        recommendations.append(
            "Improve attendance"
        )

    recommendations.append(
        "Follow daily planner"
    )

    return recommendations




# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )

# ==========================================
# GENERATE STUDY PLAN
# ==========================================

@app.route(
    "/generate",
    methods=["POST"]
)
def generate():

    try:

        subjects = request.form.getlist(
            "subject"
        )

        exam_dates = request.form.getlist(
            "exam_date"
        )

        difficulties = request.form.getlist(
            "difficulty"
        )

        available_hours = float(
            request.form[
                "available_hours"
            ]
        )

        difficulties = [
            int(x)
            for x in difficulties
        ]

        plan = create_study_plan(
            subjects,
            difficulties,
            exam_dates,
            available_hours
        )

        return render_template(
            "result.html",
            plan=plan
        )

    except Exception as e:

        return f"Error: {e}"


@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:

        return redirect(
            "/login"
    )
    sample = [[

    3,      # study_hours
    70,     # attendance
    7,      # sleep_hours
    4,      # motivation
    8,      # stress
    6,      # time_management
    5,      # exam_anxiety
    7       # previous_gpa

]]
    predicted_score = round(
    float(
        performance_model.predict(sample)[0]
    ),
    2
)
    
    total_hours = 24

    completed_subjects = 5

    student = {
        "study_hours": 3,
        "attendance": 70,
        "stress_level": 8,
        "motivation": 4,
        "predicted_score": predicted_score
    }

    subject_scores = {
        "Math": 45,
        "Physics": 78,
        "Programming": 55
    }

    analysis = analyze_student(
        student,
        subject_scores
    )

    return render_template(
    "/dashboard.html",
   
)

analysis = {
    "recommendations": [
        "Study Math for 2 hours daily",
        "Practice Science questions"
    ]
}

predicted_score = 68

subject_scores = {
    "Math": 75,
    "Science": 68,
    "English": 80
}
save_history(
    "Rishi",
    predicted_score,
    str(subject_scores), 
    str(
        analysis["recommendations"]
    )
)

predicted_score = 68
total_hours = 24
completed_subjects=5,
analysis=analysis
 


@app.route("/profile")
def profile():

    return render_template(
        "profile.html"
    )


@app.route("/history")
def history():

    if "user_id" not in session:

        return redirect(
            "/login"
        )

    records = get_history(
        session["user_id"]
    )

    return render_template(
        "/history.html",
        records=records
    )

    if "user_id" not in session:

        return redirect(
            "/login"
        )

    records = get_history(

        session["user_id"]

    )

    return render_template(

        "history.html",

        records=records

    )

# ==========================================
# PERFORMANCE PREDICTION
# ==========================================

@app.route(
    "/predict_score",
    methods=["POST"]
)
def predict_score():

    try:

        study_hours = float(
            request.form["study_hours"]
        )

        attendance = float(
            request.form["attendance"]
        )

        sleep_hours = float(
            request.form["sleep_hours"]
        )

        motivation = float(
            request.form["motivation"]
        )

        stress = float(
            request.form["stress"]
        )

        time_management = float(
            request.form["time_management"]
        )

        exam_anxiety = float(
            request.form["exam_anxiety"]
        )

        previous_gpa = float(
            request.form["previous_gpa"]
        )

        data = [[

            study_hours,
            attendance,
            sleep_hours,
            motivation,
            stress,
            time_management,
            exam_anxiety,
            previous_gpa

        ]]

        prediction = performance_model.predict(
            data
        )

        return {

            "predicted_score":
            round(
                float(prediction[0]),
                2
            )
        }

    except Exception as e:

        return {
            "error": str(e)
        }

@app.route(
    "/register",
    methods=["GET","POST"]
)
def register():

    if request.method == "POST":

        username = request.form["username"]

        email = request.form["email"]

        password = request.form["password"]

        register_user(
            username,
            email,
            password
        )

        return redirect("/login")

    return render_template(
        "register.html"
    )


@app.route(
    "/login",
    methods=["GET","POST"]
)
def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        user = login_user(
            email,
            password
        )

        if user:

            session["user_id"] = user[0]

            session["username"] = user[1]

            return redirect(
                "/dashboard"
            )

        return "Invalid Credentials"

    return render_template(
        "login.html"
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

# ==========================================
# RUN APP
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )






