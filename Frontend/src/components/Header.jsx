function Header() {
  return (
    <header className="mb-10">
      <p className="font-mono text-xs tracking-[0.2em] text-brand uppercase mb-3">
        Content Review
      </p>
      <h1 className="font-display text-4xl sm:text-5xl text-ink font-medium leading-tight">
        Moderation desk
      </h1>
      <p className="mt-3 text-ink-soft text-base sm:text-lg max-w-xl">
        Submit content for automated analysis, risk assessment, and a
        moderation decision.
      </p>
    </header>
  )
}

export default Header
