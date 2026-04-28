import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("Loaded API Key:", api_key[:10] if api_key else "NOT FOUND")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-2.5-flash")


def generate_audit_report():
    print("Gemini report generation started...")

    with open("precomputed/results.json", "r") as f:
        data = json.load(f)

    bias = data["bias_overview"]
    shap = data["shap_global"]

    top_feature = shap[0]["feature"]

    prompt = f"""
You are an AI governance expert.

Generate a professional compliance audit report.

Facts:
- Fairness Score: {bias["fairness_score"]}/10
- Female shortlist rate: {bias["female_rate"]}%
- Male shortlist rate: {bias["male_rate"]}%
- Priya verdict: {bias["priya_verdict"]}
- Raj verdict: {bias["raj_verdict"]}
- Top SHAP feature: {top_feature}

Write:
1. Final Verdict
2. Executive Summary
3. Key Findings
4. Recommended Action

Keep it concise and professional.
"""

    response = model.generate_content(prompt)

    return response.text