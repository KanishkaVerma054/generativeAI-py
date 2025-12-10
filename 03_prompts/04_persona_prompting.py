# Persona Based Prompting
import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

# for OpenAI client

# client = OpenAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     base_url="https://generativelanguage.googleapis.com/v1beta/"
# )
client = OpenAI()

SYSTEM_PROMPT="""
    You are a AI Persona Assistant named Kanishk Verma.
    You are acting on behalf of Kanishk Verma who is 25 years old Tech Enthusiast and principle engineer. Your main tech stack is JS, Python and GoLang and you are learning GenAI these days.

    Examples:
    Q: Hey
    A: Hey, Whats up!
"""

response = client.chat.completions.create(
    # model="gemini-2.5-flash",
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Who are you?"}
    ]
)

print(response.choices[0].message.content)