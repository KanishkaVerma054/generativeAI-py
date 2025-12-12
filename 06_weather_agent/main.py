import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format-%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    return "Something went wrong"

def main():
    user_query = input("> ")
    responses = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_query}
        ]
    )

    print(f"🤖: {responses.choices[0].message.content}")

# main()
print(get_weather("delhi"))