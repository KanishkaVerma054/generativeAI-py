from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# for OpenAI client
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Hey, I am Kanishk! Nice to meet you!"}
    ]
)

print[response.choices[0].message.content]