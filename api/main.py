from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import uuid

app = FastAPI(title="AI Business Platform", version="1.0.0")

class TaskRequest(BaseModel):
    description: str
    complexity: str
    dependencies: List[str] = []
    parameters: Dict[str, Any] = {}

class TaskResponse(BaseModel):
    task_id: str
    status: str
    result: Dict[str, Any] = {}

# Initialize orchestrator and agents
orchestrator = TaskOrchestrator()
strategic_agent = StrategicAgent("strategy_001")
synthetic_agent = SyntheticAgent("synthetic_001")

orchestrator.register_agent(strategic_agent)
orchestrator.register_agent(synthetic_agent)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(orchestrator.process_tasks())

@app.post("/tasks", response_model=TaskResponse)
async def create_task(task_request: TaskRequest):
    task_id = str(uuid.uuid4())
    task = Task(
        id=task_id,
        description=task_request.description,
        complexity=task_request.complexity,
        dependencies=task_request.dependencies,
        parameters=task_request.parameters
    )
    
    await orchestrator.submit_task(task)
    
    return TaskResponse(
        task_id=task_id,
        status="submitted"
    )

@app.get("/tasks/{task_id}")
async def get_task_result(task_id: str):
    if task_id not in orchestrator.results_store:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return orchestrator.results_store[task_id]

@app.get("/agents")
async def get_agents():
    return {
        "agents": [
            {
                "agent_id": agent.agent_id,
                "capabilities": agent.capabilities,
                "available": agent.is_available
            }
            for agent in orchestrator.agents.values()
        ]
    }
