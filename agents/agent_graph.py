from langchain.agents import create_agent
import os
from dotenv import load_dotenv
from tools import system_tool as st

load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

def browser_agent():
    """This is a specialized agent for browser related work"""
    agent1 = create_agent(
        model="google_genai:gemini-2.5-flash-lite",
        tools=[],
        system_prompt='You are a helpful assistant'

    )
def iot_agent():
    """This is a specialized agent for iot related work"""
    agent2 = create_agent(
        model="google_genai:gemini-2.5-flash-lite",
        tools=[],
        system_prompt='You are a helpful assistant'

    )

def search_agent():
    """This is a specialized agent for search related work"""
    agent3 = create_agent(
        model="google_genai:gemini-2.5-flash-lite",
        tools=[],
        system_prompt='You are a helpful assistant'

    )

def system_agent(query:str):
    """
    This is a specialized agent for system related work.
    Input should be the specific task to perform.
    Example open "YouTube" or open "Instagram"
    """
    agent4 = create_agent(
        model="google_genai:gemini-2.5-flash-lite",
        tools=[st.open_youtube,st.open_instagram,st.open_github],
        system_prompt='You control system applications and browser actions.'

    )
    agent4.invoke({"input": query})




def vision_agent():
    """This is a specialized agent for vision related work"""
    agent5 = create_agent(
        model="google_genai:gemini-2.5-flash-lite",
        tools=[],
        system_prompt='You are a helpful assistant'

    )