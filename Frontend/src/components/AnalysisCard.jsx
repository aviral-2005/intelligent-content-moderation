function Stat({ label, value }) {
  return (
    <div>
      <p className="text-xs text-ink-soft uppercase tracking-wide">{label}</p>
      <p className="font-mono text-sm text-ink mt-1">{value}</p>
    </div>
  )
}

function AnalysisCard({ analysis }) {
  const {
    original_content,
    word_count,
    character_count,
    language,
    sentiment,
    keywords = [],
    tone,
    quality_score,
  } = analysis

  return (
    <section className="bg-panel border border-line rounded-2xl shadow-sm p-6 sm:p-8">
      <p className="font-mono text-xs tracking-[0.2em] text-brand uppercase mb-4">
        01 · Content Analysis
      </p>

      <blockquote className="text-ink text-sm sm:text-base leading-relaxed border-l-2 border-line pl-4 mb-6">
        {original_content}
      </blockquote>

      <div className="grid grid-cols-2 sm:grid-cols-4 gap-y-5 gap-x-4 mb-6">
        <Stat label="Word count" value={word_count} />
        <Stat label="Character count" value={character_count} />
        <Stat label="Language" value={language} />
        <Stat label="Sentiment" value={sentiment} />
        <Stat label="Tone" value={tone} />
        <Stat label="Quality score" value={quality_score} />
      </div>

      {keywords.length > 0 && (
        <div>
          <p className="text-xs text-ink-soft uppercase tracking-wide mb-2">
            Keywords
          </p>
          <div className="flex flex-wrap gap-2">
            {keywords.map((keyword) => (
              <span
                key={keyword}
                className="rounded-full bg-brand-soft text-brand-dark text-xs font-medium px-3 py-1"
              >
                {keyword}
              </span>
            ))}
          </div>
        </div>
      )}
    </section>
  )
}

export default AnalysisCard
