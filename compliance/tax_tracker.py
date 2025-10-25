class TaxTracker:
    def __init__(self):
        self.tax_rates = {
            'ZA': 0.15,  # VAT in South Africa
            'US': 0.10,  # Estimated average
            'EU': 0.20,  # VAT average
            'AU': 0.10,  # GST
            'NA': 0.15,  # Namibia VAT
            'BW': 0.12   # Botswana VAT
        }
    
    async def calculate_tax_obligations(self, revenue_data: Dict[str, float]) -> Dict[str, Any]:
        """Calculate tax obligations by country"""
        tax_obligations = {}
        total_tax = 0
        
        for country, revenue in revenue_data.items():
            tax_rate = self.tax_rates.get(country, 0.15)
            tax_amount = revenue * tax_rate
            tax_obligations[country] = {
                'revenue': revenue,
                'tax_rate': tax_rate,
                'tax_amount': tax_amount,
                'deadline': await self._get_tax_deadline(country)
            }
            total_tax += tax_amount
        
        return {
            'total_tax_obligation': total_tax,
            'breakdown_by_country': tax_obligations,
            'reminders': await self._generate_tax_reminders(tax_obligations)
        }
    
    async def _generate_tax_reminders(self, tax_data: Dict[str, Any]) -> List[str]:
        """Generate tax payment reminders for owner"""
        reminders = []
        current_date = datetime.now()
        
        for country, data in tax_data.items():
            deadline = data['deadline']
            days_until_deadline = (deadline - current_date).days
            
            if days_until_deadline <= 30:
                reminders.append(
                    f"⚠️ Tax payment for {country} due in {days_until_deadline} days. "
                    f"Amount: ZAR {data['tax_amount']:,.2f}"
                )
        
        return reminders
