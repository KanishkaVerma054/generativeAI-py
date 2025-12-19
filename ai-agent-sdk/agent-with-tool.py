from dotenv import load_dotenv
from agents import Agent, Runner
from agents import WebSearchTool

load_dotenv()

# Defining an agent
hello_agent = Agent(
    name="Hello World Agent",
    instructions="You're an agent which greets the user and helps them ans using emojis and in funny way",
    tools=[
        WebSearchTool() # Hosted tool by openAI
    ]
)

result = Runner.run_sync(hello_agent, "Hey can you please fetch the weather information of Saharsa, Bihar 852201")

print(result.final_output)