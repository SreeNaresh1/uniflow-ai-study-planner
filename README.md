# UniFlow: AI Study Planner & Exam Copilot

UniFlow is an AI-powered multi-agent assistant that converts a student's syllabus 
into a personalized study plan, provides daily guidance, and explains concepts 
using Gemini models and the Google Agent Development Kit (ADK).

This project includes:

✔ A Planner Agent  
✔ A Tutor Agent  
✔ A Review Agent  
✔ A Multi-agent Orchestrator  
✔ Custom tools for syllabus parsing + scheduling  
✔ A lightweight Cloud Run API deployment  

---

## 1. Features (Exactly as implemented)

### ✔ Convert raw syllabus text into structured topics  
Using a custom tool `parse_syllabus()`.

### ✔ Generate a personalized study plan  
Using `compute_schedule()` and ADK tool-calling.

### ✔ Provide daily study guidance  
Using the Review Agent.

### ✔ Explain any topic with examples  
Using the Tutor Agent (Gemini 2.0 Flash).

### ✔ Multi-agent coordination  
Orchestrator Agent routes queries to the right sub-agent.

### ✔ Cloud Run Deployment  
Simple Flask app acting as UniFlow API endpoint.

---

## 2. System Architecture

User
│
▼
Orchestrator Agent
├── Planner Agent
├── Tutor Agent
└── Review Agent
│
▼
Memory (STUDY_PLANS, PROGRESS_LOGS)

---

## 3. Tools

- **parse_syllabus(raw_text)**  
- **compute_schedule(topics, start_date, exam_date, daily_hours)**

These were implemented exactly as in the notebook.

---

## 4. ADK Runner Usage

The notebook used:

- InMemoryRunner
- Session service
- Synchronous `runner.run(...)`

A helper `ask()` function was created for testing.

---

## 5. Deployment (Cloud Run)

We deployed the API using:

gcloud run deploy uniflow-agent
--source .
--region us-central1
--allow-unauthenticated
--set-env-vars GOOGLE_API_KEY=XXX

---

## 6. Demo Examples

### Example 1: Creating a Study Plan
Input:
Binary Trees
AVL Trees
Heaps
My exam is on 2025-11-25. I can study 2 hours per day.

Output:
- Binary Trees today
- AVL Trees tomorrow
- Heaps next day

### Example 2: Daily Guidance
What should I study today?

### Example 3: Concept Explanation
Explain AVL tree rotations with an example.

---

## 7. Notebook

The full UniFlow implementation (agents, tools, demo) is available in:

**`uniflow_notebook.ipynb`**

This matches exactly what was executed in Kaggle.

---

## 8. API Endpoint (After Deployment)

POST https://uniflow-agent-xxx.a.run.app/uniflow
{
"message": "Explain AVL rotations"
}

---

## 9. Requirements

flask
google-genai
google-adk
nest_asyncio

---

## 10. Limitations

- No persistent database (memory only)
- Fixed 2-hour per topic estimation
- Simple greedy scheduler
- Basic Cloud Run backend

---

## 11. License
MIT License
