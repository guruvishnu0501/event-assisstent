import os
from google import genai

# 1. Setup - You'll need to set your API key in your environment later
# For now, we are building the logic structure
client = genai.Client(api_key="YOUR_API_KEY_HERE")

class SmartEventAssistant:
    def __init__(self):
        self.context = """
        You are a helpful AI assistant for the 'Global AI Summit 2026'.
        Event Details:
        - Location: Hall 5, Convention Center.
        - WiFi: 'AI_Summit_Guest' (Password: Welcome2026).
        - Keynote: 10:00 AM by the CTO of Google.
        - Lunch: 1:00 PM in the Food Court.
        - Help Desk: Located near the main entrance.
        """

    def get_answer(self, user_prompt):
        # Combining context with user question to ensure logical decision making
        full_prompt = f"{self.context}\n\nUser Question: {user_prompt}\nAssistant:"
        
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=full_prompt
        )
        return response.text

if __name__ == "__main__":
    assistant = SmartEventAssistant()
    
    # Example simulation for the challenge
    question = "What's the WiFi password and where can I eat?"
    print(f"Attendee: {question}")
    
    # In a real submission, we'd handle the API key securely
    try:
        print(f"Assistant: {assistant.get_answer(question)}")
    except Exception as e:
        print("Assistant: [API Key not configured, but logic is ready!]")