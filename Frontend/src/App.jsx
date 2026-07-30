import { useState } from 'react'
import Header from './components/Header'
import ModerationForm from './components/ModerationForm'
import AnalysisCard from './components/AnalysisCard'
import RiskCard from './components/RiskCard'
import DecisionCard from './components/DecisionCard'
import { moderateContent } from './services/api'

function App() {
  const [result, setResult] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleSubmit = async (content) => {
    setIsLoading(true)
    setError(null)
    setResult(null)

    try {
      const data = await moderateContent(content)
      setResult(data)
    } catch (err) {
      setError(
        err.response?.data?.detail ||
          err.message ||
          'Something went wrong while analyzing this content.'
      )
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen">
      <main className="max-w-3xl mx-auto px-4 sm:px-6 py-12 sm:py-16">
        <Header />

        <ModerationForm onSubmit={handleSubmit} isLoading={isLoading} />

        {error && (
          <div
            role="alert"
            className="mt-6 rounded-xl border border-risk-high-border bg-risk-high-bg px-4 py-3 text-sm text-risk-high"
          >
            <p className="font-medium">Analysis failed</p>
            <p className="mt-0.5 text-risk-high/90">{error}</p>
          </div>
        )}

        {result && (
          <div className="mt-8 space-y-6">
            <AnalysisCard analysis={result.analysis} />
            <RiskCard risk={result.risk} />
            <DecisionCard decision={result.decision} />
          </div>
        )}
      </main>
    </div>
  )
}

export default App
