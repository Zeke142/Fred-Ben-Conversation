import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

frontend_system = "You are a frontend web designer. Focus on layout, responsiveness, accessibility, and UI development. Avoid backend logic."
backend_system = "You are a backend specialist. Focus on API design, database structure, and authentication. Avoid frontend layout."

# Initial message from the Frontend bot
frontend_msg = "I need the `/users` API to return `username` and `avatar URL` for the dashboard profile cards."

def get_gpt_response(system_prompt, user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

# Simulate conversation
print("🟦 Frontend GPT:", frontend_msg)
for _ in range(5):  # Change the range for longer convos
    backend_msg = get_gpt_response(backend_system, frontend_msg)
    print("\n🟧 Backend GPT:", backend_msg)

    frontend_msg = get_gpt_response(frontend_system, backend_msg)
    print("\n🟦 Frontend GPT:", frontend_msg)
