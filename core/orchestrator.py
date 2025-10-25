class TaskOrchestrator:
    def __init__(self):
        self.agents = {}
        self.task_queue = asyncio.Queue()
        self.results_store = {}
        self.logger = logging.getLogger("TaskOrchestrator")
    
    def register_agent(self, agent: BaseAIAgent):
        self.agents[agent.agent_id] = agent
        self.logger.info(f"Registered agent: {agent.agent_id}")
    
    async def submit_task(self, task: Task) -> str:
        await self.task_queue.put(task)
        self.logger.info(f"Submitted task: {task.id}")
        return task.id
    
    async def process_tasks(self):
        while True:
            task = await self.task_queue.get()
            await self._dispatch_task(task)
            self.task_queue.task_done()
    
    async def _dispatch_task(self, task: Task):
        suitable_agents = [
            agent for agent in self.agents.values() 
            if agent.can_handle(task) and agent.is_available
        ]
        
        if suitable_agents:
            # Select the most appropriate agent
            selected_agent = suitable_agents[0]  # Could implement more sophisticated selection
            selected_agent.is_available = False
            
            try:
                result = await selected_agent.execute_task(task)
                self.results_store[task.id] = {
                    "status": "completed",
                    "result": result,
                    "agent_id": selected_agent.agent_id
                }
            except Exception as e:
                self.results_store[task.id] = {
                    "status": "failed",
                    "error": str(e)
                }
            finally:
                selected_agent.is_available = True
        else:
            self.results_store[task.id] = {
                "status": "failed",
                "error": "No suitable agent available"
            }
