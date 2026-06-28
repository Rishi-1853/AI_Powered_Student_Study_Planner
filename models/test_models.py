import joblib

model = joblib.load(
    "models/priority_model.pkl"
)

print(model.feature_names_in_)
