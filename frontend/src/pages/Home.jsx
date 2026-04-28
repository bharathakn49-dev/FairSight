import { useNavigate } from 'react-router-dom'

export default function Home() {
  const navigate = useNavigate()

  return (
    <div className="max-w-4xl mx-auto px-6 py-24 text-center">

      <div className="inline-flex items-center gap-2 bg-red-50 border border-red-200
      text-red-700 text-sm font-medium px-4 py-2 rounded-full mb-8">
        <span className="w-2 h-2 bg-red-500 rounded-full animate-pulse"></span>
        Live Case Study — AI Hiring Bias
      </div>

      <h1 className="text-5xl font-bold text-slate-900 mb-6 leading-tight">
        Why did the AI<br />
        reject her application?
      </h1>

      <p className="text-xl text-slate-500 mb-10 leading-relaxed">
        AI hiring systems reject candidates every day.
        Most people never know why.
        FairSight exposes the hidden bias.
      </p>

      <div className="bg-white rounded-2xl border border-slate-200
      p-8 shadow-sm mb-10 text-left">

        <div className="flex items-center gap-4 mb-6">
          <div className="w-12 h-12 bg-rose-100 rounded-full
          flex items-center justify-center text-xl">
            👩
          </div>

          <div>
            <p className="font-bold text-slate-900">Priya</p>
            <p className="text-sm text-slate-500">
              Software Engineer Applicant
            </p>
          </div>

          <div className="ml-auto bg-red-100 text-red-700
          font-bold text-sm px-4 py-2 rounded-full">
            REJECTED
          </div>
        </div>

        <div className="grid grid-cols-3 gap-4 mb-6">
          {[
            { label: 'Degree %', value: '61%' },
            { label: 'Test Score', value: '58' },
            { label: 'Work Experience', value: 'Yes' }
          ].map(item => (
            <div
              key={item.label}
              className="bg-slate-50 rounded-xl p-4 text-center"
            >
              <div className="text-2xl font-bold text-slate-800">
                {item.value}
              </div>
              <div className="text-sm text-slate-500 mt-1">
                {item.label}
              </div>
            </div>
          ))}
        </div>

        <p className="text-slate-600 leading-relaxed">
          Priya has good academic performance and work experience.
          Raj — an identical candidate with the same scores —
          was shortlisted.
          The only difference?
          <strong> Gender.</strong>
        </p>
      </div>

      <button
        onClick={() => navigate('/bias')}
        className="bg-slate-900 hover:bg-slate-800 text-white
        text-lg font-semibold px-12 py-4 rounded-xl
        transition-all shadow-lg"
      >
        Audit the AI Model →
      </button>

      <p className="text-slate-400 text-sm mt-4">
        Powered by SHAP · Gemini · FastAPI
      </p>
    </div>
  )
}
