import { riskLevelClasses } from '../utils/riskLevel'

function RiskBadge({ level }) {
  return (
    <span
      className={`inline-flex items-center rounded-md border px-2.5 py-1 text-xs font-medium ${riskLevelClasses(level)}`}
    >
      {level}
    </span>
  )
}

function RiskRow({ label, level }) {
  return (
    <div className="flex items-center justify-between py-2.5 border-b border-line last:border-b-0">
      <span className="text-sm text-ink-soft">{label}</span>
      <RiskBadge level={level} />
    </div>
  )
}

function RiskCard({ risk }) {
  const {
    overall_risk_score,
    overall_risk_level,
    spam_risk,
    policy_risk,
    legal_risk,
    brand_risk,
    confidence,
    reasoning,
    recommended_action,
  } = risk

  return (
    <section className="bg-panel border border-line rounded-2xl shadow-sm p-6 sm:p-8">
      <p className="font-mono text-xs tracking-[0.2em] text-brand uppercase mb-4">
        02 · Risk Assessment
      </p>

      <div className="flex items-center justify-between mb-6">
        <div>
          <p className="text-xs text-ink-soft uppercase tracking-wide mb-1">
            Overall risk
          </p>
          <div className="flex items-center gap-3">
            <RiskBadge level={overall_risk_level} />
            <span className="font-mono text-sm text-ink-soft">
              score {overall_risk_score}
            </span>
          </div>
        </div>
        <div className="text-right">
          <p className="text-xs text-ink-soft uppercase tracking-wide mb-1">
            Confidence
          </p>
          <p className="font-mono text-sm text-ink">{confidence}</p>
        </div>
      </div>

      <div className="mb-6">
        <RiskRow label="Spam risk" level={spam_risk} />
        <RiskRow label="Policy risk" level={policy_risk} />
        <RiskRow label="Legal risk" level={legal_risk} />
        <RiskRow label="Brand risk" level={brand_risk} />
      </div>

      {reasoning && (
        <div className="mb-4">
          <p className="text-xs text-ink-soft uppercase tracking-wide mb-1">
            Reasoning
          </p>
          <p className="text-sm text-ink leading-relaxed">{reasoning}</p>
        </div>
      )}

      {recommended_action && (
        <div>
          <p className="text-xs text-ink-soft uppercase tracking-wide mb-1">
            Recommended action
          </p>
          <p className="text-sm text-ink font-medium">{recommended_action}</p>
        </div>
      )}
    </section>
  )
}

export default RiskCard
