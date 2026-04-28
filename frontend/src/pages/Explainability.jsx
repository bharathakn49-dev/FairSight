import { useEffect, useState } from 'react'
import axios from 'axios'

export default function Explainability() {
  const [data, setData] = useState(null)

  useEffect(() => {
    axios.get('/api/shap-global')
      .then((res) => {
        console.log(res.data)
        setData(res.data)
      })
      .catch((err) => {
        console.error("API Error:", err)
      })
  }, [])

  if (!data) {
    return (
      <div className="max-w-4xl mx-auto px-6 py-20">
        <h1 className="text-2xl font-bold text-slate-900 mb-4">
          Loading Explainability Data...
        </h1>
        <p className="text-slate-500">
          Fetching SHAP analysis from backend.
        </p>
      </div>
    )
  }

  return (
    <div className="max-w-5xl mx-auto px-6 py-16">

      <div className="mb-10">
        <p className="text-sm font-semibold text-emerald-600 uppercase tracking-wide">
          Explainable AI
        </p>

        <h1 className="text-4xl font-bold text-slate-900 mt-2 mb-3">
          Why Was Priya Rejected?
        </h1>

        <p className="text-lg text-slate-500">
          SHAP reveals which features most strongly influenced the hiring decision
        </p>
      </div>

      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-8">
        <h2 className="text-2xl font-bold text-slate-900 mb-6">
          Global Feature Importance
        </h2>

        <div className="space-y-4">

          {Array.isArray(data) && data.slice(0, 8).map((item, index) => (
            <div
              key={index}
              className="border border-slate-200 rounded-xl p-5"
            >
              <div className="flex items-center justify-between mb-3">

                <div>
                  <p className="text-sm text-slate-400">
                    Rank #{index + 1}
                  </p>

                  <h3 className="text-lg font-bold text-slate-900">
                    {item.feature}
                  </h3>
                </div>

                <div className={`px-4 py-2 rounded-full text-sm font-semibold ${
                  index === 0
                    ? 'bg-red-100 text-red-700'
                    : 'bg-slate-100 text-slate-700'
                }`}>
                  Importance: {item.importance}
                </div>

              </div>

              {index === 0 && (
                <p className="text-red-600 font-medium">
                  Highest-impact feature → strongest evidence of discrimination
                </p>
              )}
            </div>
          ))}

        </div>
      </div>

    </div>
  )
}