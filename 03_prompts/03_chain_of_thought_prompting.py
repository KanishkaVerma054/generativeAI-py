# Chain of thought Prompting
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

SYSTEM_PROMPT = f"""
    You are an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to think first PLAN what need to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN(That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

    Output JSON Format:
    {{ "step": "START" | "PLAN" | "OUTPUT", "content": "string" }}

    Example:
    START: {{"step": "START", "content": "Hey, Can you write a code to solve 2 + 3 * 5 / 10"}}
    PLAN: {{"step": "PLAN", "content": "Seems like user is intrested in maths problem"}}
    PLAN: {{"step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method"}}
    PLAN: {{"step": "PLAN", "content": "Yes, The BODMAS is corrrect thing to be done here"}}
    PLAN: {{"step": "PLAN", "content": "first we multiple 3 * 5 which is 15"}}
    PLAN: {{"step": "PLAN", "content": "Now equation is 2 + 15 / 10"}}
    PLAN: {{"step": "PLAN", "content": "We must perform divide that is 15 / 10 = 1.5"}}
    PLAN: {{"step": "PLAN", "content": "Now the new equation is 2 + 1.5"}}
    PLAN: {{"step": "PLAN", "content": "Now finally let's perform the add 3.5"}}
    PLAN: {{"step": "PLAN", "content": "GREAT, we have solved and finally left with 3.5 as ans"}}
    OUTPUT: {{"step": "PLAN", "3.5"}}
"""

print("\n\n")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input("👉 ")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=message_history
    )
    raw_result= response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})

    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("🔥", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "PLAN":
        print("🧠", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        break

print("\n\n")

# response = client.chat.completions.create(
#     # model="gemini-2.5-flash",
#     model="gpt-4o-mini",
#     response_format={"type": "json_object"},
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user", "content": "Hey, write a code to add n number in js"},
#         # Manually keep adding messages to the history
#         {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "User wants to create a JavaScript code that can add an arbitrary number of values."})},
#         {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "To accomplish this, we can use the rest parameter syntax in JavaScript to handle multiple inputs."})},
#         {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Next, we need to ensure the function takes these inputs and calculates their sum."})},
#         {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "We can create a simple function called `addNumbers` that takes any number of arguments and returns their sum using the `reduce` method."})},
#         {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Let's finalize the code structure for the function."})},
#     ]
# )

# print(response.choices[0].message.content)