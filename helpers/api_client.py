import requests
from config.settings import BASE_URL

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()

    def get_all_products(self):
        url = f"{self.base_url}productsList"
        response = self.session.get(url)
        print(f"Request URL: {url}, Response Status: {response.status_code}")
        return response

    def post_to_all_products(self):
        url = f"{self.base_url}productsList"
        response = self.session.post(url)
        print(f"Request URL: {url}, Response Status: {response.status_code}")
        return response

    def get_all_brands(self):
        url = f"{self.base_url}brandsList"
        response = self.session.get(url)
        print(f"Request URL: {url}, Response Status: {response.status_code}")
        return response
