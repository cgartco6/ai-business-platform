import os
from dataclasses import dataclass

@dataclass
class AIConfig:
    # Agent Configuration
    MAX_CONCURRENT_TASKS: int = 10
    AGENT_TIMEOUT: int = 300  # seconds
    
    # Strategic Intelligence
    RISK_THRESHOLD: float = 0.7
    OPTIMIZATION_ITERATIONS: int = 1000
    
    # Synthetic Intelligence
    CREATIVITY_TEMPERATURE: float = 0.8
    MAX_GENERATION_LENGTH: int = 1000
    
    # API Configuration
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

@dataclass
class ModelConfig:
    STRATEGIC_MODEL: str = "gpt-3.5-turbo"
    SYNTHETIC_MODEL: str = "gpt-4"
    EMBEDDING_MODEL: str = "text-embedding-ada-002"
