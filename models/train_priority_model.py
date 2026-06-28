import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ====================================
# LOAD DATASET
# ====================================

df = pd.read_csv(
    "dataset/cleaned_study_planner_dataset.csv"
)

# ====================================
# CREATE PRIORITY LABEL
# ====================================

def create_priority(score):

    if score < 60:
        return "High"

    elif score < 80:
        return "Medium"

    else:
        return "Low"


df["priority"] = df[
    "exam_score"
].apply(create_priority)

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

X = df[features]

y = df["priority"]

# ====================================
# SPLIT
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

model = RandomForestClassifier(
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

accuracy = accuracy_score(
    y_test,
    pred
)

print("\nPriority Model Results")
print("-" * 40)

print(
    "Accuracy:",
    round(
        accuracy * 100,
        2
    ),
    "%"
)

# ====================================
# SAVE MODEL
# ====================================

joblib.dump(
    model,
    "models/priority_model.pkl"
)

joblib.dump(
    features,
    "models/priority_columns.pkl"
)

print("\nPriority Model Saved")