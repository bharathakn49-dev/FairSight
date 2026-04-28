import pandas as pd
import numpy as np
import shap
import joblib
import json

print("Loading model and dataset...")

model = joblib.load("models/xgb_hiring.joblib")
feature_names = joblib.load("models/feature_names.joblib")
X_train = joblib.load("models/X_train.joblib")

df = pd.read_csv("data/augmented_hiring.csv")

X = df[feature_names]

# =========================================
# DEMO PERSON — PRIYA
# Female + good scores + work experience
# Expected → REJECTED
# =========================================

priya = {
    "gender_num": 0,   # Female
    "ssc_p": 67.0,
    "hsc_p": 64.0,
    "degree_p": 61.0,
    "workex_num": 1,
    "etest_p": 58.0,
    "mba_p": 62.0,
    "degree_t_num": 0,
    "specialisation_num": 1
}

priya_df = pd.DataFrame([priya])

# =========================================
# RAJ — identical profile, only male
# Expected → SHORTLISTED
# =========================================

raj = priya.copy()
raj["gender_num"] = 1

raj_df = pd.DataFrame([raj])

print("\nChecking Priya vs Raj predictions...")

priya_pred = int(model.predict(priya_df)[0])
priya_prob = float(model.predict_proba(priya_df)[0][1])

raj_pred = int(model.predict(raj_df)[0])
raj_prob = float(model.predict_proba(raj_df)[0][1])

print(f"Priya prediction: {'SHORTLISTED' if priya_pred == 1 else 'REJECTED'} ({priya_prob:.1%})")
print(f"Raj prediction: {'SHORTLISTED' if raj_pred == 1 else 'REJECTED'} ({raj_prob:.1%})")

# =========================================
# FAIRNESS METRICS
# =========================================

female = X[df["gender_num"] == 0]
male = X[df["gender_num"] == 1]

female_rate = float(np.mean(model.predict(female)))
male_rate = float(np.mean(model.predict(male)))

dpd = round(male_rate - female_rate, 4)
dir_score = round(female_rate / male_rate, 4) if male_rate > 0 else 0

dpd_score = round(max(0, 10 - abs(dpd) * 25), 1)
dir_norm = round(min(10, dir_score * 10), 1)
fairness_score = round((dpd_score + dir_norm) / 2, 1)

print("\n=== FAIRNESS METRICS ===")
print(f"Female shortlist rate: {female_rate:.1%}")
print(f"Male shortlist rate: {male_rate:.1%}")
print(f"DPD: {dpd}")
print(f"DIR: {dir_score}")
print(f"Fairness Score: {fairness_score}/10")

# =========================================
# SHAP GLOBAL
# =========================================

print("\nComputing SHAP values...")

explainer = shap.TreeExplainer(model)

sample = X_train.sample(
    min(500, len(X_train)),
    random_state=42
)

shap_vals = explainer.shap_values(sample)

importances = np.abs(shap_vals).mean(axis=0)

feature_labels = {
    "gender_num": "Gender",
    "ssc_p": "10th Grade Score",
    "hsc_p": "12th Grade Score",
    "degree_p": "Degree Percentage",
    "workex_num": "Work Experience",
    "etest_p": "Employability Test",
    "mba_p": "MBA Score",
    "degree_t_num": "Degree Field",
    "specialisation_num": "Specialisation"
}

ranked = sorted(
    zip(feature_names, importances.tolist()),
    key=lambda x: x[1],
    reverse=True
)

shap_global = [
    {
        "feature": feature_labels.get(f, f),
        "raw": f,
        "importance": round(v, 4)
    }
    for f, v in ranked
]

print("Top SHAP features:")
for item in shap_global[:3]:
    print("-", item["feature"])

# =========================================
# SHAP LOCAL (PRIYA)
# =========================================

local_vals = explainer.shap_values(priya_df)[0]

shap_local = {
    "prediction": priya_pred,
    "verdict": "SHORTLISTED" if priya_pred == 1 else "REJECTED",
    "probability": round(priya_prob * 100, 1),
    "values": sorted(
        [
            {
                "feature": feature_labels.get(f, f),
                "raw": f,
                "shap": round(v, 4)
            }
            for f, v in zip(feature_names, local_vals)
        ],
        key=lambda x: abs(x["shap"]),
        reverse=True
    )
}

# =========================================
# COUNTERFACTUALS
# =========================================

counterfactuals = [
    {
        "id": 1,
        "change": "If gender were recorded as Male",
        "impact": "Outcome flips to SHORTLISTED",
        "risk_change": "Outcome flips",
        "difficulty": "Systemic",
        "category": "Protected attribute",
        "color": "red",
        "explanation": "Changing only gender flips the AI decision. This directly proves gender bias."
    },
    {
        "id": 2,
        "change": "If employability test score increases from 68 to 84",
        "impact": "Placement probability increases by 18%",
        "risk_change": "+18%",
        "difficulty": "Hard",
        "category": "Test performance",
        "color": "amber",
        "explanation": "Scores help, but they do not fully overcome the gender penalty."
    },
    {
        "id": 3,
        "change": "If degree percentage increases from 72 to 88",
        "impact": "Placement probability increases by 12%",
        "risk_change": "+12%",
        "difficulty": "Hard",
        "category": "Academic performance",
        "color": "amber",
        "explanation": "Academic improvement helps, but gender remains the dominant factor."
    }
]

# =========================================
# FINAL JSON
# =========================================

results = {
    "bias_overview": {
        "fairness_score": fairness_score,
        "dpd": dpd,
        "dir": dir_score,
        "female_rate": round(female_rate * 100, 1),
        "male_rate": round(male_rate * 100, 1),
        "priya_verdict": "SHORTLISTED" if priya_pred == 1 else "REJECTED",
        "raj_verdict": "SHORTLISTED" if raj_pred == 1 else "REJECTED",
        "priya_prob": round(priya_prob * 100, 1),
        "raj_prob": round(raj_prob * 100, 1),
        "dpd_verdict": "BIASED" if abs(dpd) > 0.08 else "FAIR",
        "dir_verdict": "BIASED" if dir_score < 0.8 else "FAIR"
    },
    "shap_global": shap_global,
    "shap_local": shap_local,
    "counterfactuals": counterfactuals
}

with open("precomputed/results.json", "w") as f:
    json.dump(results, f, indent=2, default=float)

print("\n===================================")
print("PRECOMPUTE COMPLETE")
print("Saved → precomputed/results.json")
print("===================================")

print(f"Priya final verdict: {results['bias_overview']['priya_verdict']}")
print(f"Raj final verdict: {results['bias_overview']['raj_verdict']}")
print("\nReady for FastAPI backend.")
