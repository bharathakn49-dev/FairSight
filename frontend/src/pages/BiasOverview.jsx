import { useEffect, useState } from 'react'
import axios from 'axios'

export default function BiasOverview() {
  const [data, setData] = useState(null)

  useEffect(() => {
    axios.get('/api/bias-overview')
      .then(res => {
        setData(res.data)
      })
      .catch(err => {
        console.error(err)
      })
  }, [])

  if (!data) {
    return (
      <div className="p-10 text-center text-slate-500">
        Loading fairness audit...
      </div>
    )
  }

  return (
    <div className="max-w-6xl mx-auto px-6 py-16">

      <div className="mb-10">
        <p className="text-sm font-semibold text-emerald-600 uppercase tracking-wide">
          Fairness Audit
        </p>

        <h1 className="text-4xl font-bold text-slate-900 mt-2 mb-3">
          Bias Detection Results
        </h1>

        <p className="text-lg text-slate-500">
          Pre-deployment fairness audit for automated hiring decisions
        </p>
      </div>

      {/* Top Cards */}
      <div className="grid md:grid-cols-3 gap-6 mb-10">

        <div className="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
          <p className="text-sm text-slate-500 mb-2">
            Fairness Score
          </p>

          <h2 className="text-5xl font-bold text-slate-900">
            {data.fairness_score}/10
          </h2>

          <p className="text-sm text-slate-400 mt-3">
            Lower score means stronger discrimination detected
          </p>
        </div>

        <div className="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
          <p className="text-sm text-slate-500 mb-2">
            Demographic Parity Difference
          </p>

          <h2 className="text-4xl font-bold text-red-600">
            {data.dpd}
          </h2>

          <p className="text-sm text-slate-400 mt-3">
            Verdict: {data.dpd_verdict}
          </p>
        </div>

        <div className="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
          <p className="text-sm text-slate-500 mb-2">
            Disparate Impact Ratio
          </p>

          <h2 className="text-4xl font-bold text-red-600">
            {data.dir}
          </h2>

          <p className="text-sm text-slate-400 mt-3">
            Verdict: {data.dir_verdict}
          </p>
        </div>
      </div>

      {/* Priya vs Raj */}
      <div className="bg-white rounded-2xl border border-slate-200 p-8 shadow-sm mb-10">
        <h2 className="text-2xl font-bold text-slate-900 mb-6">
          Counterfactual Proof of Bias
        </h2>

        <div className="grid md:grid-cols-2 gap-6">

          <div className="rounded-xl border border-red-200 bg-red-50 p-6">
            <p className="text-sm text-slate-500 mb-2">Candidate A</p>

            <h3 className="text-xl font-bold mb-2">
              Priya
            </h3>

            <p className="text-red-700 font-bold text-lg">
              {data.priya_verdict}
            </p>

            <p className="text-sm text-slate-600 mt-2">
              Placement Probability: {data.priya_prob}%
            </p>
          </div>

          <div className="rounded-xl border border-emerald-200 bg-emerald-50 p-6">
            <p className="text-sm text-slate-500 mb-2">Candidate B</p>

            <h3 className="text-xl font-bold mb-2">
              Raj
            </h3>

            <p className="text-emerald-700 font-bold text-lg">
              {data.raj_verdict}
            </p>

            <p className="text-sm text-slate-600 mt-2">
              Placement Probability: {data.raj_prob}%
            </p>
          </div>

        </div>

        <p className="mt-6 text-slate-600 leading-relaxed">
          Both candidates have identical academic performance and work experience.
          The only changed feature is <strong>gender</strong>.
          The AI decision flips completely.
        </p>
      </div>

      {/* Group Comparison */}
      <div className="bg-white rounded-2xl border border-slate-200 p-8 shadow-sm">
        <h2 className="text-2xl font-bold text-slate-900 mb-6">
          Group-Level Shortlist Rates
        </h2>

        <div className="grid md:grid-cols-2 gap-6">

          <div className="rounded-xl bg-slate-50 p-6">
            <p className="text-sm text-slate-500 mb-2">
              Female Candidates
            </p>

            <h3 className="text-4xl font-bold text-red-600">
              {data.female_rate}%
            </h3>
          </div>

          <div className="rounded-xl bg-slate-50 p-6">
            <p className="text-sm text-slate-500 mb-2">
              Male Candidates
            </p>

            <h3 className="text-4xl font-bold text-emerald-600">
              {data.male_rate}%
            </h3>
          </div>

        </div>
      </div>

    </div>
  )
}