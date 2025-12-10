# Few Shot prompting
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# for OpenAI client
client = OpenAI()
# client = OpenAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     base_url="https://generativelanguage.googleapis.com/v1beta/"
# )

# Few Shot prompting: Directly giving the instruction and few examples to the model
SYSTEM_PROMPT = f"""
You should only and only ans coding realted questions. Do not ans anything else. Your name is Alexa. If user ask you something other than coding, just say sorry.

Rule:
- Strictly follow the output in JSON format

Output Format:
{{
    "code": "string or null,
    "isCodingQuestion": boolean
}}

Examples:
Q: Can you explain the a + b whole square?
A: {{"code": "null", "isCodingQuestion": false}}

Q: Hey, Write a code in pyhton for adding two numbers.
A: {{
    "code": "def add(a, b):
        return a + b",
    "isCodingQuestion": false
}}
"""

response = client.chat.completions.create(
    # model="gemini-2.5-flash",
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, write a code to add n number in js"}
    ]
)

print(response.choices[0].message.content)

# Few-shot Prompting: The model is provided with a few examples before asking it to generate a response.