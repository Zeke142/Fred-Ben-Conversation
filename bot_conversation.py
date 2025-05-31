from openai import OpenAI
from dotenv import load_dotenv
import os

# ⛔ DO NOT copy your API key into this chat ⛔
# ✅ Paste your real key below directly in GitHub (never here)
client = OpenAI(
    api_key="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"
)

def get_gpt_response(system_prompt, user_msg):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_msg}
        ]
    )
    return response.choices[0].message.content

# Define system prompts
frontend_system = "You are Fred, a frontend web designer. Be concise and focus on user interface and user experience."
backend_system = "You are Ben, a backend specialist. Focus on data models, endpoints, and server logic."

# Start the conversation
frontend_msg = "I need the `/users` API to return `username` and `avatar URL` for the dashboard profile cards."
print(f"🟦 Fred (Frontend): {frontend_msg}")

backend_msg = get_gpt_response(backend_system, frontend_msg)
print(f"🟫 Ben (Backend): {backend_msg}")

frontend_reply = get_gpt_response(frontend_system, backend_msg)
print(f"🟦 Fred (Frontend): {frontend_reply}")
