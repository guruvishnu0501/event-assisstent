# VibeForge - Smart Event Navigator
**Vertical:** Physical Event Experience

## 🚀 Approach
This solution uses an Agentic AI pattern to assist physical event attendees. Instead of static FAQ responses, it uses the `google-genai` (Gemini 2.0 Flash) model to interpret user intent and provide context-aware guidance.

## 🧠 Logic Flow
1. **Context Loading:** The assistant is bootstrapped with a specific event 'knowledge base' (Hall locations, WiFi, Schedule).
2. **Intent Parsing:** When a user asks a question, the LLM determines if they need navigation, technical help, or scheduling info.
3. **Response Generation:** The model generates a natural language response grounded strictly in the provided event details.

## 🛠 Google Services Integration
- **Gemini 2.0 Flash API:** Used for natural language understanding and real-time reasoning.
- **Google Antigravity:** Development and scaffolding environment.

## 🔐 Security & Best Practices
- **Environment Variables:** Designed to use `.env` for API keys to prevent exposure (added to `.gitignore`).
- **Resource Efficiency:** Minimal dependency weight to keep the repository under 1 MB.