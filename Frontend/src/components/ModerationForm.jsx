import { useState } from 'react'
import LoadingSpinner from './LoadingSpinner'

function ModerationForm({ onSubmit, isLoading }) {
  const [content, setContent] = useState('')

  const handleSubmit = (event) => {
    event.preventDefault()
    if (!content.trim() || isLoading) return
    onSubmit(content)
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-panel border border-line rounded-2xl shadow-sm p-6 sm:p-8"
    >
      <label htmlFor="content" className="sr-only">
        Content to analyze
      </label>
      <textarea
        id="content"
        name="content"
        value={content}
        onChange={(event) => setContent(event.target.value)}
        placeholder="Enter content to analyze..."
        rows={7}
        disabled={isLoading}
        className="w-full resize-y rounded-xl border border-line bg-paper px-4 py-3 text-ink placeholder:text-ink-soft/60 focus:outline-none focus:ring-2 focus:ring-brand/40 focus:border-brand transition-colors disabled:opacity-60"
      />

      <div className="mt-4 flex items-center justify-between">
        <span className="font-mono text-xs text-ink-soft">
          {content.length.toLocaleString()} characters
        </span>

        <button
          type="submit"
          disabled={isLoading || !content.trim()}
          className="inline-flex items-center gap-2 rounded-lg bg-brand px-5 py-2.5 text-sm font-medium text-white hover:bg-brand-hover transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {isLoading && <LoadingSpinner />}
          {isLoading ? 'Analyzing...' : 'Analyze Content'}
        </button>
      </div>
    </form>
  )
}

export default ModerationForm
