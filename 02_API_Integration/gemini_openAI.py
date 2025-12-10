import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# for OpenAI client
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", "content": "Hey, I am Kanishk! Nice to meet you!"}
    ]
)

print(response.choices[0].message.content)