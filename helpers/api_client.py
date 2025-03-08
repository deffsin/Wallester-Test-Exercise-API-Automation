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

    def put_to_all_brands(self):
        url = f"{self.base_url}brandsList"
        response = self.session.put(url)
        print(f"Request URL: {url}, Response Status: {response.status_code}")
        return response

    def post_to_search_product(self, search_product):
        url = f"{self.base_url}searchProduct"
        payload = {"search_product": search_product}
        response = self.session.post(url, data=payload) # post s parametrom
        print(f"Request URL: {url}, Response Status: {response.status_code}, Response: {response.text}")
        return response

    def post_to_search_product_without_parameter(self):
        url = f"{self.base_url}searchProduct"
        response = self.session.post(url, data={}) # pustoj data otpravljaem
        print(f"Request URL: {url}, Response Status: {response.status_code}, Response: {response.text}")
        return response
