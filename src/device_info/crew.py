import os
from typing import List
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from src.device_info.tools.custom_tool import SystemInfo
from langchain_openai import ChatOpenAI 

os.environ["OPENAI_API_KEY"] = "NA"
llm = LLM(model="ollama/mistral:7b", 
        provider="ollama",
        base_url="http://localhost:11434",
        stream=False,
)

@CrewBase
class DeviceInfo():
    """DeviceInfo crew"""

    agents: List[BaseAgent]
    tasks: List[Task]



    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'],
            verbose=True,
            tools=[SystemInfo()],
            llm=llm,
            step_callback=lambda step: print(f"Agent Step: {step}"),
            allow_delegation=False,
        )


    @task
    def answer_query(self) -> Task:
        return Task(
            config=self.tasks_config['answer_query']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the DeviceInfo crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
            process=Process.sequential,
        )
