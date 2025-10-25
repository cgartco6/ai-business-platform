class RevenueTracker:
    def __init__(self):
        self.revenue_data = {}
        self.geo_data = {}
        self.product_analytics = {}
    
    async def track_revenue(self, payment_data: Dict[str, Any]):
        """Track revenue from payments"""
        country = payment_data.get('country', 'Unknown')
        amount = payment_data.get('amount', 0)
        product = payment_data.get('product', 'unknown')
        
        # Update revenue by country
        if country not in self.revenue_data:
            self.revenue_data[country] = 0
        self.revenue_data[country] += amount
        
        # Update product analytics
        if product not in self.product_analytics:
            self.product_analytics[product] = {'revenue': 0, 'customers': 0}
        self.product_analytics[product]['revenue'] += amount
        self.product_analytics[product]['customers'] += 1
        
        # Update geo data
        await self._update_geo_analytics(country, amount)
    
    async def get_business_insights(self) -> Dict[str, Any]:
        """Generate comprehensive business insights"""
        total_revenue = sum(self.revenue_data.values())
        target_revenue = 1000000  # 1 million ZAR
        
        insights = {
            'current_revenue': total_revenue,
            'target_revenue': target_revenue,
            'progress_percentage': (total_revenue / target_revenue) * 100,
            'top_performing_countries': await self._get_top_countries(),
            'revenue_trends': await self._analyze_revenue_trends(),
            'customer_acquisition': await self._analyze_customer_growth(),
            'projected_earnings': await self._project_earnings(),
            'recommendations': await self._generate_recommendations()
        }
        
        return insights

class OwnerDashboard:
    def __init__(self):
        self.revenue_tracker = RevenueTracker()
        self.security = MilitaryGradeSecurity()
    
    async def get_dashboard_data(self, owner_token: str) -> Dict[str, Any]:
        """Get secure dashboard data for owner"""
        # Verify owner access
        try:
            payload = self.security.verify_token(owner_token)
            if payload.get('role') != 'owner':
                raise Exception("Unauthorized access")
        except Exception as e:
            raise Exception("Invalid owner token")
        
        dashboard_data = {
            'financials': {
                'current_balance': await self._get_current_balance(),
                'weekly_revenue': await self._get_weekly_revenue(),
                'monthly_target': 1000000,
                'payout_schedule': await self._get_payout_schedule()
            },
            'subscribers': {
                'total': await self._get_total_subscribers(),
                'active': await self._get_active_subscribers(),
                'new_today': await self._get_new_subscribers_today(),
                'churn_rate': await self._calculate_churn_rate()
            },
            'geographic_analysis': await self.revenue_tracker.get_business_insights(),
            'content_performance': await self._get_content_performance(),
            'system_health': await self._get_system_health()
        }
        
        return dashboard_data
