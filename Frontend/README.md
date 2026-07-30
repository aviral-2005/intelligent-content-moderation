# Moderation Desk — Content Review Frontend

A minimal, professional frontend for the Intelligent Content Review &
Moderation Workflow. Submits content to a FastAPI backend and renders the
returned analysis, risk assessment, and moderation decision.

This is a **frontend-only** project. It expects the backend to already be
running and reachable — it does not implement, mock, or simulate any of the
AI/business logic itself.

## Tech stack

- React 19 + Vite
- JavaScript (no TypeScript)
- Tailwind CSS v4
- Axios

## Backend requirement

The app calls:

```
POST http://localhost:8000/moderate
```

with body `{ "content": "..." }`, and expects the `analysis` / `risk` /
`decision` response shape described in the project brief. Start your FastAPI
backend on `localhost:8000` before using the app. If your backend runs on a
different host/port, update `baseURL` in `src/services/api.js`.

## Install

```bash
npm install
```

## Run (development)

```bash
npm run dev
```

Then open the printed local URL (defaults to http://localhost:5173).

## Build for production

```bash
npm run build
npm run preview
```

## Project structure

```
src/
  components/
    Header.jsx          — page title and subtitle
    ModerationForm.jsx   — textarea + submit button, loading state
    AnalysisCard.jsx     — renders the "analysis" section
    RiskCard.jsx         — renders the "risk" section with colored badges
    DecisionCard.jsx     — renders the "decision" section (verdict card)
    LoadingSpinner.jsx   — small reusable spinner
  services/
    api.js               — axios client + moderateContent()
  utils/
    riskLevel.js          — Low/Medium/High and decision -> color mapping
  App.jsx
  index.css              — Tailwind import + design tokens
```

## Notes

- No routing, no authentication — a single page.
- All data shown comes directly from the backend's `/moderate` response;
  nothing is mocked.
- If the request to the backend fails (network error, non-2xx response), a
  clean inline alert is shown instead of crashing.
