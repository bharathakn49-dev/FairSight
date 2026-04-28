from gemini_report import generate_audit_report
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(
    title="FairSight API",
    version="1.0.0"
)

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load precomputed results once
with open("precomputed/results.json", "r") as f:
    DATA = json.load(f)

@app.get("/")
def root():
    return {
        "message": "FairSight API is running",
        "docs": "/docs"
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "message": "Backend is healthy"
    }

@app.get("/api/bias-overview")
def bias_overview():
    return DATA["bias_overview"]

@app.get("/api/shap-global")
def shap_global():
    return DATA["shap_global"]

@app.get("/api/shap-local")
def shap_local():
    return DATA["shap_local"]

@app.get("/api/counterfactual")
def counterfactual():
    return DATA["counterfactuals"]

@app.get("/api/gemini-report")
def gemini_report():
    report = generate_audit_report()

    return {
        "report": report
    }
