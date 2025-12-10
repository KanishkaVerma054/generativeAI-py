from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Hey, I am Kanishk! Nice to meet you!"
)
print(response.text)