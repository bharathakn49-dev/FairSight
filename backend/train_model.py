import pandas as pd
import joblib

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

print("Loading augmented dataset...")

df = pd.read_csv("data/augmented_hiring.csv")

print(f"Total rows loaded: {len(df)}")

# Features used for prediction
feature_names = [
    'gender_num',
    'ssc_p',
    'hsc_p',
    'degree_p',
    'workex_num',
    'etest_p',
    'mba_p',
    'degree_t_num',
    'specialisation_num'
]

# Input features
X = df[feature_names]

# Target output
# 1 = placed / shortlisted
# 0 = rejected
y = df['status_num']

print("\nSplitting train/test data...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print(f"Training rows: {len(X_train)}")
print(f"Testing rows: {len(X_test)}")

print("\nTraining XGBoost model...")

model = XGBClassifier(
    n_estimators=40,
    max_depth=2,
    learning_rate=0.08,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    eval_metric='logloss'
)

model.fit(X_train, y_train)

print("\nEvaluating model...")

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"\n=== MODEL TRAINING COMPLETE ===")
print(f"Accuracy: {accuracy:.3f}")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Save model files
joblib.dump(model, "models/xgb_hiring.joblib")
joblib.dump(feature_names, "models/feature_names.joblib")
joblib.dump(X_train, "models/X_train.joblib")
joblib.dump(X_test, "models/X_test.joblib")
joblib.dump(y_test, "models/y_test.joblib")

print("\nSaved files:")
print("models/xgb_hiring.joblib")
print("models/feature_names.joblib")
print("models/X_train.joblib")
print("models/X_test.joblib")
print("models/y_test.joblib")

print("\nModel is ready for fairness audit.")
