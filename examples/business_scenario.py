import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.agents.base_agent import StrategicAgent, SyntheticAgent, Task
from core.orchestrator import TaskOrchestrator

async def run_business_scenario():
    # Initialize system
    orchestrator = TaskOrchestrator()
    
    # Register agents
    strategy_agent = StrategicAgent("business_strategist_1")
    synthetic_agent = SyntheticAgent("creative_solver_1")
    
    orchestrator.register_agent(strategy_agent)
    orchestrator.register_agent(synthetic_agent)
    
    # Start task processing
    processor_task = asyncio.create_task(orchestrator.process_tasks())
    
    # Submit complex business tasks
    tasks = [
        Task(
            id="task_1",
            description="Analyze market trends and provide strategic recommendations for AI adoption",
            complexity="high",
            dependencies=[],
            parameters={"market_sector": "technology", "timeframe": "2024"}
        ),
        Task(
            id="task_2", 
            description="Generate innovative business models for AI service delivery",
            complexity="medium",
            dependencies=[],
            parameters={"industry": "consulting", "target_audience": "enterprise"}
        )
    ]
    
    # Submit all tasks
    for task in tasks:
        await orchestrator.submit_task(task)
    
    # Wait for tasks to complete
    await asyncio.sleep(5)
    
    # Check results
    for task in tasks:
        if task.id in orchestrator.results_store:
            result = orchestrator.results_store[task.id]
            print(f"Task {task.id}: {result['status']}")
            if result['status'] == 'completed':
                print(f"Result: {result['result']}")
    
    # Cleanup
    processor_task.cancel()

if __name__ == "__main__":
    asyncio.run(run_business_scenario())
