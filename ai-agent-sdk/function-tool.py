from dotenv import load_dotenv
import requests
from agents import Agent, Runner
from agents import WebSearchTool, function_tool

load_dotenv()

@function_tool()
def get_weather(city: str):
    """Fetch the weather for a given city name.
    Args:
        city: The city name to fetch the weather for.

    """

    url = f"https://wttr.in/{city.lower()}?format-%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    return "Something went wrong"

# Defining an agent
hello_agent = Agent(
    name="Hello World Agent",
    instructions="You're an agent which greets the user and helps them ans using emojis and in funny way",
    tools=[
        # WebSearchTool(), # Hosted tool by openAI
        get_weather
    ]
)

result = Runner.run_sync(hello_agent, "Hey can you please fetch the weather information of Saharsa, Bihar 852201")

print(result.final_output)