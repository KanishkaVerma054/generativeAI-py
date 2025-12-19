from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()

# Defining an agent
hello_agent = Agent(
    name="Hello World Agent",
    instructions="You're an agent which greets the user and helps them ans using emojis and in funny way"
)

result = Runner.run_sync(hello_agent, "Hey there, my name is Kanishk")

print(result.final_output)