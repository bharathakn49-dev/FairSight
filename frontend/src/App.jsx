import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Home from './pages/Home'
import BiasOverview from './pages/BiasOverview'
import Explainability from './pages/Explainability'
import AuditReport from './pages/AuditReport'

export default function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-slate-50">
        <Navbar />

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/bias" element={<BiasOverview />} />
          <Route path="/explain" element={<Explainability />} />
          <Route path="/report" element={<AuditReport />} />
        </Routes>

      </div>
    </BrowserRouter>
  )
}