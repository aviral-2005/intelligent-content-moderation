/**
 * Maps a risk level string ("Low" | "Medium" | "High") to the Tailwind
 * classes used to render its badge. Falls back to a neutral style for
 * any value the backend hasn't defined yet.
 */
export function riskLevelClasses(level) {
  const normalized = (level || '').toLowerCase()

  if (normalized === 'low') {
    return 'text-risk-low bg-risk-low-bg border-risk-low-border'
  }
  if (normalized === 'medium') {
    return 'text-risk-medium bg-risk-medium-bg border-risk-medium-border'
  }
  if (normalized === 'high') {
    return 'text-risk-high bg-risk-high-bg border-risk-high-border'
  }
  return 'text-ink-soft bg-line/40 border-line'
}

/**
 * Maps a moderation decision string to the classes used for the
 * verdict card's accent border, text color, and background wash.
 */
export function decisionClasses(decision) {
  const normalized = (decision || '').toLowerCase()

  if (normalized === 'approved') {
    return {
      border: 'border-risk-low',
      text: 'text-risk-low',
      bg: 'bg-risk-low-bg',
    }
  }
  if (normalized === 'rejected') {
    return {
      border: 'border-risk-high',
      text: 'text-risk-high',
      bg: 'bg-risk-high-bg',
    }
  }
  // "Human Review Required" and any other in-between outcome
  return {
    border: 'border-risk-medium',
    text: 'text-risk-medium',
    bg: 'bg-risk-medium-bg',
  }
}
