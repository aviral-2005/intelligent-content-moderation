Moderation Workflow

An AI-powered content moderation system that analyzes user-generated content, assesses potential risks, and provides intelligent moderation decisions using a multi-agent workflow.

Developed as part of a **Generative AI internship project** to explore Agentic AI workflows using **LangGraph**, **FastAPI**, **React**, and **Google Gemini**.

---

## 🚀 Features

- 📝 AI-powered Content Analysis
- ⚠️ Intelligent Risk Assessment
- 🤖 Automated Moderation Decision
- 🔄 Multi-Agent Workflow using LangGraph
- 🌐 REST API built with FastAPI
- 💻 Modern React Dashboard
- 🎨 Responsive UI with Tailwind CSS
- 📊 Structured Risk & Decision Reports
- ⚡ Real-time Backend ↔ Frontend Integration
- 🛡️ Centralized Exception Handling

---

## 🏗️ Project Architecture

```
                    User
                      │
                      ▼
             React Frontend (Vite)
                      │
              POST /moderate
                      │
                      ▼
               FastAPI Backend
                      │
                      ▼
          LangGraph Moderation Workflow
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
Content Analyzer   Risk Assessor   Review Coordinator
                      │
                      ▼
              Final Moderation Decision
                      │
                      ▼
             JSON Response to Frontend
```

---

## 🛠️ Tech Stack

### Backend

- Python
- FastAPI
- LangGraph
- LangChain
- Google Gemini API
- Pydantic

### Frontend

- React
- Vite
- Tailwind CSS
- Axios

---

## 📂 Project Structure

```
intelligent-content-moderation/
│
├── backend/
│   ├── agents/
│   ├── graph/
│   ├── routers/
│   ├── models/
│   ├── utils/
│   ├── exceptions/
│   ├── data/
│   ├── api.py
│   ├── main.py
│   ├── config.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/intelligent-content-moderation.git

cd intelligent-content-moderation
```

---

## 🔹 Backend Setup

```bash
cd backend

python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Run the backend

```bash
uvicorn api:app --reload
```

Backend runs on

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

---

## 🔹 Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

## 📡 API Endpoint

### POST `/moderate`

### Request

```json
{
  "content": "I absolutely love this product."
}
```

### Response

```json
{
  "analysis": {
    "original_content": "...",
    "word_count": 10,
    "character_count": 70,
    "language": "English",
    "sentiment": "Positive",
    "keywords": [],
    "tone": "Friendly",
    "quality_score": 0.95
  },
  "risk": {
    "overall_risk_score": 0.12,
    "overall_risk_level": "Low",
    "spam_risk": "Low",
    "policy_risk": "Low",
    "legal_risk": "Low",
    "brand_risk": "Low",
    "confidence": 0.95,
    "reasoning": "...",
    "recommended_action": "Approve"
  },
  "decision": {
    "decision": "Approved",
    "reason": "...",
    "confidence": 0.95,
    "recommended_action": "Approve"
  }
}
```

---

## 📸 Screenshots

<img width="1653" height="865" alt="image" src="https://github.com/user-attachments/assets/860a847c-f11f-4bb9-816b-b47349ebac22" />
<img width="1651" height="857" alt="image" src="https://github.com/user-attachments/assets/fd4da3b7-d333-4abf-ab30-240bf8dc6860" />


Example:

```
screenshots/
├── home.png
├── analysis.png
├── risk.png
└── decision.png
```

---

## 🎯 Future Improvements

- Human-in-the-Loop Review Workflow
- User Authentication
- Moderation History Database
- Analytics Dashboard
- Role-Based Access Control
- Docker Support
- CI/CD Pipeline
- Cloud Deployment
- Audit Logs
- Batch Content Moderation

---

## 📚 Key Concepts Demonstrated

- Agentic AI Workflow
- Multi-Agent Systems
- LangGraph State Management
- LLM Integration
- Prompt Engineering
- REST API Development
- Frontend–Backend Integration
- Modular Software Architecture
- Exception Handling
- API Design
- Component-Based React Development

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Aviral Tripathi**

B.Tech – Computer Science & Data Science

GitHub: https://github.com/aviral-2005

LinkedIn: www.linkedin.com/in/aviral-tripathi-951465202
---

⭐ If you found this project useful, consider giving it a star!
