from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")

# Check if API key loaded properly
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment. Make sure your .env file is set.")

# Create the OpenAI client
client = OpenAI(api_key=api_key)

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
