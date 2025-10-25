import tweepy
import requests
from facebook_business import FacebookSession, FacebookAdsApi
from facebook_business.adobjects.user import User
import asyncio
from typing import Dict, Any

class SocialMediaAutoPoster:
    def __init__(self):
        self.platform_clients = {}
        self.setup_clients()
    
    def setup_clients(self):
        """Initialize social media API clients"""
        # Twitter/X
        self.platform_clients['twitter'] = tweepy.Client(
            bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
            consumer_key=os.getenv('TWITTER_API_KEY'),
            consumer_secret=os.getenv('TWITTER_API_SECRET'),
            access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
            access_token_secret=os.getenv('TWITTER_ACCESS_SECRET')
        )
        
        # Facebook/Instagram
        session = FacebookSession(
            os.getenv('FACEBOOK_APP_ID'),
            os.getenv('FACEBOOK_APP_SECRET'),
            os.getenv('FACEBOOK_ACCESS_TOKEN')
        )
        FacebookAdsApi.set_default_api(FacebookAdsApi(session))
    
    async def auto_post_content(self, content: Dict[str, Any]):
        """Automatically post content to all platforms"""
        platform = content['platform']
        content_data = content['content']
        
        try:
            if platform == 'twitter':
                await self._post_to_twitter(content_data)
            elif platform == 'facebook':
                await self._post_to_facebook(content_data)
            elif platform == 'instagram':
                await self._post_to_instagram(content_data)
            elif platform == 'tiktok':
                await self._post_to_tiktok(content_data)
            elif platform == 'youtube':
                await self._post_to_youtube(content_data)
            
            print(f"✅ Successfully posted to {platform}")
            
        except Exception as e:
            print(f"❌ Failed to post to {platform}: {str(e)}")
            await self._handle_posting_error(platform, content_data, str(e))
    
    async def _post_to_twitter(self, content: Dict[str, Any]):
        """Post to Twitter/X"""
        client = self.platform_clients['twitter']
        
        # Post text
        tweet = client.create_tweet(text=content['script'])
        
        # Post media if available
        if content.get('visuals'):
            media_ids = []
            for visual in content['visuals'][:4]:  # Twitter allows max 4 media
                media = client.media_upload(visual)
                media_ids.append(media.media_id)
            
            if media_ids:
                client.create_tweet(
                    text=content['script'],
                    media_ids=media_ids
                )
    
    async def _post_to_instagram(self, content: Dict[str, Any]):
        """Post to Instagram"""
        user = User('me')
        
        # Create container for photo/video
        if content.get('final_content'):
            container = user.containers.create(
                image_url=content['final_content'],
                caption=content['script']
            )
            
            # Publish the container
            user.media_publish(container_id=container['id'])

class ViralContentOptimizer:
    def __init__(self):
        self.engagement_metrics = {}
        self.performance_data = {}
    
    async def optimize_content_strategy(self):
        """Continuously optimize content based on performance"""
        trending_topics = await self._get_trending_topics()
        best_performers = await self._analyze_best_performers()
        
        optimization_recommendations = {
            'best_times_to_post': await self._calculate_optimal_times(),
            'top_performing_formats': await self._identify_winning_formats(),
            'audience_preferences': await self._analyze_audience_behavior(),
            'content_improvements': await self._suggest_content_improvements()
        }
        
        return optimization_recommendations
