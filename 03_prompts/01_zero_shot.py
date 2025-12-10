# Zero Shot prompting
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# for OpenAI client
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Zero Shot prompting: Directly giving the instruction to the model
SYSTEM_PROMPT = "You should only and only ans coding realted questions. Do not ans anything else. Your name is Alexa. If user ask you something other than coding, just say sorry."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, can you write a pyhton code to translate the word hindi"}
    ]
)

print(response.choices[0].message.content)

# Zero Shot prompting: The model is given a direct question or task without prior examples.