from openai import OpenAI
from dotenv import load_dotenv
import os
import time

# Load .env variables (make sure you have OPENAI_API_KEY set)
load_dotenv()
client = OpenAI()

# Define system messages for Fred (frontend) and Ben (backend)
frontend_system = "You are Fred, a frontend web designer. Keep responses focused on UI/UX and frontend needs."
backend_system = "You are Ben, a backend specialist. Keep responses focused on APIs, databases, and server logic."

# Function to get a GPT response
def get_gpt_response(system_prompt, user_message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content

# Initial message from Fred
frontend_msg = "I need the `/users` API to return `username` and `avatar URL` for the dashboard profile cards."

# Let the bots talk to each other
for i in range(3):
    print(f"\n🟦 Fred (Frontend): {frontend_msg}")
    backend_msg = get_gpt_response(backend_system, frontend_msg)
    print(f"🟧 Ben (Backend): {backend_msg}")
    frontend_msg = get_gpt_response(frontend_system, backend_msg)
    time.sleep(1)
