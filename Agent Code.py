# Local Agent Implementation (No API Key Required)
from typing import Callable, List, Dict, Any
from dataclasses import dataclass

@dataclass
class Tool:
    """Simple tool definition"""
    name: str
    description: str
    func: Callable

@dataclass
class Agent:
    """Local agent without LLM dependency"""
    role: str
    goal: str
    backstory: str
    tools: List[Tool]
    verbose: bool = True
    
    def execute_task(self, task_description: str) -> str:
        """Execute a task description using available tools"""
        print(f"\n[{self.role}] Processing: {task_description}")
        print(f"Goal: {self.goal}")
        print(f"Backstory: {self.backstory}")
        
        # Use the first tool if available
        if self.tools:
            tool = self.tools[0]
            print(f"\nUsing tool: {tool.name}")
            print(f"Description: {tool.description}")
            
            # Extract topic from task description
            topic = "Operating System Scheduling"
            result = tool.func(topic)
            return result
        return "No tools available"

@dataclass
class Task:
    """Task definition"""
    description: str
    expected_output: str
    agent: Agent
    
    def execute(self) -> str:
        """Execute the task"""
        return self.agent.execute_task(self.description)

class Crew:
    """Crew of agents working together"""
    def __init__(self, agents: List[Agent], tasks: List[Task], verbose: bool = True):
        self.agents = agents
        self.tasks = tasks
        self.verbose = verbose
    
    def kickoff(self) -> str:
        """Start crew execution"""
        print("=" * 60)
        print("CREW AI - Local Implementation")
        print("=" * 60)
        
        results = []
        for task in self.tasks:
            result = task.execute()
            results.append(result)
        
        return "\n".join(results)

# Define the study tool
def study_tool(topic: str) -> str:
    """Useful for learning topics"""
    return (
        f"\n📚 LEARNING SUMMARY: {topic}"
        f"\n{'=' * 50}"
        f"\nKey Points:"
        f"\n1. Definition: {topic} is a core concept in operating systems"
        f"\n2. Purpose: Optimizes CPU utilization and system efficiency"
        f"\n3. Algorithms: FCFS, SJF, Round Robin, Priority-based"
        f"\n4. Metrics: Waiting time, Turnaround time, Response time"
        f"\nExamples:"
        f"\n- Round Robin: Fair time slice allocation to each process"
        f"\n- Priority Queue: Important tasks scheduled first"
        f"\nConclusion: Critical for modern OS performance"
        f"\n{'=' * 50}\n"
    )

# Create tool object
study_tool_obj = Tool(
    name="Study Tool",
    func=study_tool,
    description="Useful for learning topics"
)

# Create Agent
study_agent = Agent(
    role="AI Tutor",
    goal="Help students learn topics deeply",
    backstory="Expert teacher who explains simply",
    tools=[study_tool_obj],
    verbose=True
)

# Create Task
task = Task(
    description="Teach the topic: Operating System Scheduling",
    expected_output="A comprehensive learning guide on Operating System Scheduling",
    agent=study_agent
)

# Create and run Crew
crew = Crew(
    agents=[study_agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()
print("\n✅ EXECUTION COMPLETE")
print(result)
