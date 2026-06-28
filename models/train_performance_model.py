import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# ====================================
# LOAD DATASET
# ====================================

df = pd.read_csv(
    "dataset/cleaned_study_planner_dataset.csv"
)

# ====================================
# FEATURES
# ====================================

features = [
    "study_hours_per_day",
    "attendance_percentage",
    "sleep_hours",
    "motivation_level",
    "stress_level",
    "time_management_score",
    "exam_anxiety_score",
    "previous_gpa"
]

target = "exam_score"

X = df[features]
y = df[target]

# ====================================
# SPLIT DATA
# ====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ====================================
# TRAIN MODEL
# ====================================

model = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# ====================================
# EVALUATE
# ====================================

pred = model.predict(X_test)

print("\nPerformance Model Results")
print("-" * 40)

print(
    "R2 Score:",
    round(
        r2_score(
            y_test,
            pred
        ),
        4
    )
)

print(
    "MAE:",
    round(
        mean_absolute_error(
            y_test,
            pred
        ),
        4
    )
)

# ====================================
# SAVE MODEL
# ====================================

joblib.dump(
    model,
    "models/performance_model.pkl"
)

joblib.dump(
    features,
    "models/model_columns.pkl"
)

print("\nPerformance Model Saved")