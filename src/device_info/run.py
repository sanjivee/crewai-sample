from langchain_core.tools import tool
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

import litellm
litellm.set_verbose = True
# Load environment variables
load_dotenv()

# Initialize the language model
llm = ChatOpenAI(
    model="ollama/llama3.2:latest",
    base_url=os.getenv("LLM_BASE_URL")
)

import logging

logging.basicConfig(level=logging.DEBUG)


from crewai.tools import BaseTool
import json

class SystemInfo(BaseTool):
    name: str = "system_info"
    description: str = (
        "Returns current system information including battery percentage, memory, and CPU details"
    )

    def _run(self) -> str:
        return json.dumps({"battery": "50%", "memory": "16GB", "cpu": "Intel i7"})


@tool
def lookup_definition(key: str) -> str:
    """Retrieve the definition of a given key from the dictionary."""
    return sample_dict.get(key.lower(), "Key not found in the dictionary.")


# Define the agent
dictionary_agent = Agent(
    role="Dictionary Expert",
    goal="Provide value for the keys in dict",
    backstory="An expert dict lookup.",
    tools=[SystemInfo()],
    allow_delegation=False,
    memory=True,
    verbose=True,
    llm=llm
)

# Define the task
user_query = "What is the battery value?"
task = Task(
    description=user_query,
    agent=dictionary_agent,
    expected_output="Definition of the term."
)

# Create and run the crew
crew = Crew(
    agents=[dictionary_agent],
    tasks=[task],
    verbose=True
)

# Execute the task
result = crew.kickoff()
print(f"Answer: {result}")
