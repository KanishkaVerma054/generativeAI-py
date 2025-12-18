import os
from dotenv import load_dotenv
from typing_extensions import Annotated, TypedDict
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.mongodb import MongoDBSaver

load_dotenv()

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return { "messages": [response] }

graph_builder = StateGraph(State)

# Working
# state = { message: ["Hey there"]}
# node runs: chatbot(state: ["Hey there"]) -> ["Hi, This is a message from ChatBot Node"]
graph_builder.add_node("chatbot", chatbot)

# FLow:
# (START) -> chatbot -> (END)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

def compile_graph_with_checkpointer(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)

# DB_URI = "mongodb://admin:admin@localhost:27017/"
# with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:
with MongoDBSaver.from_conn_string(os.getenv("DB_URI")) as checkpointer:
    graph_with_checkpointer = compile_graph_with_checkpointer(checkpointer=checkpointer)

    # Checkpointer (Kanishk) = Hey, My name is Kanishk Verma
    config = {
        "configurable": {
            "thread_id": "Kanishk"
        }
    }

    for chunk in graph_with_checkpointer.stream(
        State({"messages": ["You know that I am learning langgraph"]}),
        config,
        stream_mode="values",
    ):
        chunk["messages"][-1].pretty_print()