import os
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class BusinessConfig:
    # Business Targets
    TARGET_SUBSCRIBERS_WEEK_1: int = 10000
    TARGET_MONTHLY_REVENUE: int = 1000000  # 1 million ZAR
    PAYOUT_DISTRIBUTION: Dict[str, float] = {
        'owner': 0.6,
        'ai_fund': 0.2,
        'reserve': 0.2
    }
    
    # Course Configuration
    COURSE_CATEGORIES: List[str] = [
        'ai_trading', 'cryptocurrency', 'forex_trading', 'stock_market',
        'business_automation', 'digital_marketing', 'content_creation'
    ]
    
    # Marketing Configuration
    SOCIAL_MEDIA_PLATFORMS: List[str] = [
        'tiktok', 'instagram', 'facebook', 'youtube', 'twitter'
    ]
    
    # Payment Configuration
    SUPPORTED_CURRENCIES: List[str] = ['ZAR', 'USD', 'EUR', 'GBP', 'AUD']
    PAYFAST_COUNTRIES: List[str] = ['ZA', 'NA', 'BW']  # Southern Africa
    
    # Security Configuration
    ENCRYPTION_ALGORITHM: str = 'AES-256-GCM'
    JWT_EXPIRY_HOURS: int = 24
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_WINDOW: int = 3600  # 1 hour

@dataclass
class APIConfig:
    # Social Media APIs
    TWITTER_API_KEY: str = os.getenv('TWITTER_API_KEY')
    INSTAGRAM_ACCESS_TOKEN: str = os.getenv('INSTAGRAM_ACCESS_TOKEN')
    TIKTOK_ACCESS_TOKEN: str = os.getenv('TIKTOK_ACCESS_TOKEN')
    
    # Payment APIs
    STRIPE_SECRET_KEY: str = os.getenv('STRIPE_SECRET_KEY')
    PAYFAST_MERCHANT_ID: str = os.getenv('PAYFAST_MERCHANT_ID')
    PAYFAST_MERCHANT_KEY: str = os.getenv('PAYFAST_MERCHANT_KEY')
    
    # Bank Account Details (Encrypted)
    FNB_ACCOUNT_OWNER: str = os.getenv('FNB_ACCOUNT_OWNER_ENCRYPTED')
    FNB_ACCOUNT_RESERVE: str = os.getenv('FNB_ACCOUNT_RESERVE_ENCRYPTED')
    RMB_ACCOUNT_AI_FUND: str = os.getenv('RMB_ACCOUNT_AI_FUND_ENCRYPTED')
