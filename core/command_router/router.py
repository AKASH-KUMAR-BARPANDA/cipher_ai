"""
command = "open YouTube"

router(command)
     ↓
cipher_agent
     ↓
agent_graph
     ↓
specific_tool
"""

from agents.cipher_agent import agent
def route_command(command):
    if command == "":
        print("Empty Command")
    else:
        agent.invoke({"messages":command})