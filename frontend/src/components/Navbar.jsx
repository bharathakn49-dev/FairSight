import { Link, useLocation } from 'react-router-dom'

const items = [
  { path: '/', label: 'Home', num: '01' },
  { path: '/bias', label: 'Bias Check', num: '02' },
  { path: '/explain', label: 'Why Rejected', num: '03' },
  { path: '/report', label: 'Audit Report', num: '04' }
]

export default function Navbar() {
  const { pathname } = useLocation()

  return (
    <nav className="bg-slate-900 px-6 py-4 flex items-center gap-8">
      <div className="flex items-center gap-2 mr-6">
        <div className="w-8 h-8 bg-emerald-500 rounded-lg flex items-center justify-center">
          <span className="text-white text-xs font-bold">FS</span>
        </div>

        <span className="text-white font-bold text-lg">
          FairSight
        </span>
      </div>

      {items.map(item => (
        <Link
          key={item.path}
          to={item.path}
          className={`flex items-center gap-2 text-sm transition-all
            ${pathname === item.path
              ? 'text-emerald-400 font-semibold'
              : 'text-slate-400 hover:text-white'
            }`}
        >
          <span className={`text-xs px-2 py-1 rounded font-mono
            ${pathname === item.path
              ? 'bg-emerald-900 text-emerald-400'
              : 'bg-slate-800 text-slate-500'
            }`}
          >
            {item.num}
          </span>

          {item.label}
        </Link>
      ))}
    </nav>
  )
}
