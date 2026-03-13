from langchain.agents import create_agent
import os
from dotenv import load_dotenv
import agents.agent_graph as ag

load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')


agent = create_agent(
    model="google_genai:gemini-2.5-flash-lite",
    tools=[ag.system_agent,ag.iot_agent,ag.search_agent,ag.vision_agent,ag.browser_agent],
    system_prompt='You are a helpful assistant',

)