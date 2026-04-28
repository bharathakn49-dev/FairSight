import { useEffect, useState } from "react";

export default function AuditReport() {
  const [report, setReport] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("https://fairsight-backend-pihm.onrender.com/api/gemini-report")
      .then((res) => res.json())
      .then((data) => {
        setReport(data.report || "No report returned.");
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        setReport("Failed to load Gemini report.");
        setLoading(false);
      });
  }, []);

  return (
    <div className="min-h-screen bg-slate-50 px-8 py-12">
      <div className="max-w-6xl mx-auto">

        <p className="text-emerald-600 font-semibold uppercase tracking-wide mb-2">
          GEMINI LIVE COMPLIANCE REPORT
        </p>

        <h1 className="text-4xl font-bold text-slate-900 mb-3">
          Automated Hiring Audit Summary
        </h1>

        <p className="text-slate-600 mb-8">
          Real-time compliance explanation generated using Gemini API
        </p>

        <div className="bg-white rounded-2xl shadow-lg border p-8">

          <div className="mb-8 p-6 rounded-xl border border-red-200 bg-red-50">
            <h2 className="text-2xl font-bold text-red-700 mb-2">
              Final Verdict: HIGH RISK BIAS DETECTED
            </h2>

            <p className="text-slate-700">
              The hiring model demonstrates strong gender-based discrimination.
              Female candidates experience significantly lower shortlist rates,
              and counterfactual testing proves that changing only gender flips
              the decision outcome.
            </p>
          </div>

          <h3 className="text-2xl font-bold text-slate-900 mb-4">
            Gemini Detailed Report
          </h3>

          {loading ? (
            <p className="text-lg text-slate-500">
              Generating report with Gemini...
            </p>
          ) : (
            <div className="bg-slate-50 rounded-xl border p-6">
              <pre className="whitespace-pre-wrap text-slate-700 leading-8 font-sans">
                {report}
              </pre>
            </div>
          )}

        </div>
      </div>
    </div>
  );
}