import asyncio
import logging
from core.agents.target_agent import TargetAgent
from marketing.autoposter import SocialMediaAutoPoster
from content_creators.manager import ContentScheduler
from core.self_healing import SelfHealingSystem

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AI-Business-Platform")

async def initialize_platform():
    """Initialize all platform components"""
    logger.info("🚀 Starting AI Business Platform...")
    
    # Initialize target agent for 10,000 subscribers
    target_agent = TargetAgent()
    target_strategy = await target_agent.achieve_targets()
    logger.info(f"🎯 Target strategy: {target_strategy}")
    
    # Start content creation and scheduling
    content_scheduler = ContentScheduler()
    content_calendar = await content_scheduler.create_content_calendar(
        topics=['AI Trading', 'Cryptocurrency', 'Business Automation'],
        platforms=['tiktok', 'instagram', 'youtube', 'facebook'],
        duration_days=30
    )
    logger.info("📅 Content calendar created for 30 days")
    
    # Start self-healing system
    healing_system = SelfHealingSystem()
    asyncio.create_task(healing_system.monitor_system_health())
    logger.info("🛡️ Self-healing system activated")
    
    # Initialize auto-poster
    autoposter = SocialMediaAutoPoster()
    logger.info("📱 Social media auto-poster ready")
    
    logger.info("✅ AI Business Platform fully operational!")
    
    return {
        'target_agent': target_agent,
        'content_scheduler': content_scheduler,
        'healing_system': healing_system,
        'autoposter': autoposter
    }

if __name__ == "__main__":
    asyncio.run(initialize_platform())
