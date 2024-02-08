from django.conf import settings
import requests

class PayStack:
    PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY
    base_url =  'https://api.paystack.co/'
    headers = {
            'Authorization': f"Bearer {PAYSTACK_SECRET_KEY}",
            "Cache-Control": "no-cache",
            'Content-Type': 'application/json'
        }

    
    @classmethod
    def generate_checkout_url(self, email, amount, ref=None, currency='NGN'):
        path = ('transaction/initialize/')

        if currency not in ['NGN', "USD", "GHS", "ZAR", "KES"]:
            currency = 'NGN'

        url = self.base_url + path
        body = {
            'email': email,
            'amount': amount,
            'currency': currency,
        }

        if ref:
            body['ref'] = ref

        response = requests.post(url, headers=self.headers, json=body)
        print(response)

        if response.status_code == 200:
            return response.json().get('data').get('authorization_url')
        
        return None
