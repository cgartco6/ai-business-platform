import hashlib
import hmac
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import jwt
from datetime import datetime, timedelta
import secrets

class MilitaryGradeSecurity:
    def __init__(self):
        self.encryption_key = os.getenv('ENCRYPTION_KEY')
        self.jwt_secret = os.getenv('JWT_SECRET')
        self.fernet = Fernet(self.encryption_key)
    
    def encrypt_data(self, data: str) -> str:
        """Encrypt sensitive data"""
        encrypted = self.fernet.encrypt(data.encode())
        return base64.urlsafe_b64encode(encrypted).decode()
    
    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt sensitive data"""
        decoded = base64.urlsafe_b64decode(encrypted_data)
        return self.fernet.decrypt(decoded).decode()
    
    def create_secure_token(self, payload: dict) -> str:
        """Create JWT token with expiration"""
        payload.update({
            'exp': datetime.utcnow() + timedelta(hours=24),
            'iat': datetime.utcnow(),
            'iss': 'ai-business-platform'
        })
        return jwt.encode(payload, self.jwt_secret, algorithm='HS256')
    
    def verify_token(self, token: str) -> dict:
        """Verify JWT token"""
        try:
            return jwt.decode(token, self.jwt_secret, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise Exception("Token expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")
    
    def hash_password(self, password: str) -> str:
        """Create secure password hash"""
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
        )
        return base64.b64encode(salt + key).decode()
    
    def verify_password(self, password: str, hashed: str) -> bool:
        """Verify password against hash"""
        decoded = base64.b64decode(hashed)
        salt = decoded[:32]
        key = decoded[32:]
        new_key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
        )
        return hmac.compare_digest(key, new_key)

class SecurityMiddleware:
    def __init__(self):
        self.security = MilitaryGradeSecurity()
        self.rate_limits = {}
    
    async def check_rate_limit(self, client_ip: str, endpoint: str) -> bool:
        """Implement rate limiting"""
        key = f"{client_ip}:{endpoint}"
        now = datetime.utcnow().timestamp()
        
        if key not in self.rate_limits:
            self.rate_limits[key] = []
        
        # Remove old requests
        self.rate_limits[key] = [t for t in self.rate_limits[key] if now - t < 3600]
        
        if len(self.rate_limits[key]) >= 100:  # 100 requests per hour
            return False
        
        self.rate_limits[key].append(now)
        return True
