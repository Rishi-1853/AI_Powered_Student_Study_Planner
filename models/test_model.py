import pandas as pd
import joblib

model = joblib.load(
    "models/performance_model.pkl"
)

columns = joblib.load(
    "models/model_columns.pkl"
)

sample = {

    "study_hours_per_day": 6,
    "attendance_percentage": 90,
    "sleep_hours": 7,
    "motivation_level": 8,
    "stress_level": 4,
    "time_management_score": 9,
    "exam_anxiety_score": 5,
    "previous_gpa": 8.2
}

sample_df = pd.DataFrame([sample])

sample_df = pd.get_dummies(
    sample_df
)

sample_df = sample_df.reindex(
    columns=columns,
    fill_value=0
)

prediction = model.predict(
    sample_df
)

print(
    f"Predicted Exam Score: {prediction[0]:.2f}"
)