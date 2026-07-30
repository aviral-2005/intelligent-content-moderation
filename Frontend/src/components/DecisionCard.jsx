import { decisionClasses } from '../utils/riskLevel'

function DecisionCard({ decision }) {
  const {
    decision: verdict,
    reason,
    confidence,
    recommended_action,
  } = decision

  const { border, text, bg } = decisionClasses(verdict)

  return (
    <section
      className={`bg-panel border-2 ${border} rounded-2xl shadow-sm overflow-hidden`}
    >
      <div className="flex flex-col sm:flex-row">
        <div className={`${bg} sm:w-56 shrink-0 flex flex-col justify-center px-6 sm:px-8 py-8 border-b sm:border-b-0 sm:border-r ${border}`}>
          <p className="font-mono text-xs tracking-[0.2em] text-ink-soft uppercase mb-2">
            03 · Decision
          </p>
          <p className={`font-display text-3xl ${text} font-medium leading-tight`}>
            {verdict}
          </p>
          {typeof confidence !== 'undefined' && (
            <p className="font-mono text-xs text-ink-soft mt-3">
              confidence {confidence}
            </p>
          )}
        </div>

        <div className="px-6 sm:px-8 py-8 flex-1 space-y-5">
          {reason && (
            <div>
              <p className="text-xs text-ink-soft uppercase tracking-wide mb-1">
                Reason
              </p>
              <p className="text-sm text-ink leading-relaxed">{reason}</p>
            </div>
          )}
          {recommended_action && (
            <div>
              <p className="text-xs text-ink-soft uppercase tracking-wide mb-1">
                Recommended action
              </p>
              <p className="text-sm text-ink font-medium">
                {recommended_action}
              </p>
            </div>
          )}
        </div>
      </div>
    </section>
  )
}

export default DecisionCard
