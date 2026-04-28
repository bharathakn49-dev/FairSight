# FairSight

## AI-Powered Hiring Bias Detection System

FairSight is an Explainable AI platform built to detect and explain bias in automated hiring decisions.

It helps organizations audit AI recruitment systems before deployment by identifying unfair decisions, demographic discrimination, and hidden bias using explainable AI and Google Gemini.

---

## Problem Statement

AI hiring systems often reject qualified candidates without transparency.

This creates serious risks:

- Gender discrimination
- Hidden algorithmic bias
- Regulatory non-compliance
- Lack of trust in automated hiring

FairSight solves this by providing fairness auditing before deployment.

---

## Core Features

### Bias Detection Dashboard

Detects whether the hiring model is biased using:

- Demographic Parity Difference
- Disparate Impact Ratio
- Fairness Score

---

### Counterfactual Bias Testing

Compares two identical candidates where only gender changes.

Example:

- Priya → Rejected
- Raj → Shortlisted

This proves discrimination through decision flipping.

---

### SHAP Explainability

Shows which features influenced the hiring decision most.

Example:

- Gender ranked as Feature #1

This provides transparent and explainable AI.

---

### Gemini Compliance Report

Google Gemini generates a leadership-ready audit summary including:

- Final risk verdict
- Executive summary
- Key findings
- Compliance exposure
- Recommended actions

This helps HR teams, legal teams, and leadership take immediate action.

---

## Tech Stack

### Frontend

- React.js
- Vite
- Tailwind CSS

### Backend

- FastAPI
- Python

### AI / ML

- SHAP Explainability
- Counterfactual Analysis
- Google Gemini API

### Cloud

- Google Cloud
- Google AI Studio

### Version Control

- Git + GitHub

---

## Project Flow

Candidate Data → Bias Detection → SHAP Analysis → Counterfactual Testing → Gemini Compliance Report

---

## Use Cases

- HR AI auditing
- Responsible AI compliance
- EU AI Act preparation
- Fair hiring validation
- Government and enterprise AI governance

---

## Demo

Prototype built for Solution Challenge 2026.

---

## Team

Built for Hackathon Submission by Team FairSight

---

## Future Scope

- Real-time enterprise integrations
- Multi-demographic fairness auditing
- Resume parser integration
- Audit PDF generation
- Google Cloud deployment
- Vertex AI production pipeline

---

## Final Verdict

FairSight turns black-box hiring AI into transparent, fair, and accountable decision-making.

Because fairness should never be optional.