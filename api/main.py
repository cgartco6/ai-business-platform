from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from security.military_grade import SecurityMiddleware, MilitaryGradeSecurity

app = FastAPI(title="AI Business Platform Pro", version="2.0.0")

# Add security middleware
app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["yourdomain.com"])

security = SecurityMiddleware()
auth = MilitaryGradeSecurity()

@app.post("/api/v1/create-course")
async def create_course(
    course_data: dict,
    authorization: str = Header(...),
    x_client_ip: str = Header(...)
):
    """Create new addictive course"""
    # Verify authentication
    try:
        payload = auth.verify_token(authorization)
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    # Check rate limit
    if not await security.check_rate_limit(x_client_ip, "create_course"):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    
    course_creator = CourseCreator()
    course = await course_creator.create_addictive_course(
        course_data['category'],
        course_data['level']
    )
    
    return {"status": "success", "course": course}

@app.get("/api/v1/owner/dashboard")
async def get_owner_dashboard(authorization: str = Header(...)):
    """Get secure owner dashboard"""
    dashboard = OwnerDashboard()
    data = await dashboard.get_dashboard_data(authorization)
    
    return {"status": "success", "dashboard": data}

@app.post("/api/v1/process-payment")
async def process_payment(payment_data: dict):
    """Process customer payment"""
    processor = PaymentProcessor()
    result = await processor.process_payment(
        payment_data['amount'],
        payment_data['currency'],
        payment_data['customer'],
        payment_data['method'],
        payment_data['country']
    )
    
    # Track revenue
    tracker = RevenueTracker()
    await tracker.track_revenue({
        'country': payment_data['country'],
        'amount': payment_data['amount'],
        'product': payment_data.get('product', 'premium_subscription')
    })
    
    return {"status": "success", "payment": result}

# Add more endpoints for content creation, social media posting, etc.
