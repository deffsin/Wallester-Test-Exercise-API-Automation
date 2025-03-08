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

    def post_to_verify_login_with_valid_details(self, email, password):
        url = f"{self.base_url}verifyLogin"
        payload = {"email": email,
                   "password": password
        }
        response = self.session.post(url, data=payload)
        print(f"Request URL: {url}, Response Status: {response.status_code}, Response: {response.text}")
        return response

    def post_to_create_user_account(self, name, email, password, title, birth_date, birth_month, birth_year,
                                    firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number):
        url = f"{self.base_url}createAccount"
        payload = {
            "name": name,
            "email": email,
            "password": password,
            "title": title,
            "birth_date": birth_date,
            "birth_month": birth_month,
            "birth_year": birth_year,
            "firstname": firstname,
            "lastname": lastname,
            "company": company,
            "address1": address1,
            "address2": address2,
            "country": country,
            "zipcode": zipcode,
            "state": state,
            "city": city,
            "mobile_number": mobile_number
        }
        response = self.session.post(url, data=payload)
        print(f"Request URL: {url}, Response Status: {response.status_code}, Response: {response.text}")
        return response

    def post_to_verify_login_without_email_parameter(self, password):
        url = f"{self.base_url}verifyLogin"
        payload = {
            "password": password
        }
        response = self.session.post(url, data=payload)
        print(f"Request URL: {url}, Response Status: {response.status_code}, Response: {response.text}")
        return response


    def delete_to_verify_login(self):
        url = f"{self.base_url}verifyLogin"
        response = self.session.delete(url)
        print(f"Request URL: {url}, Response Status: {response.status_code}, Response: {response.text}")
        return response

    def post_to_verify_login_with_invalid_details(self, email, password):
        url = f"{self.base_url}verifyLogin"
        payload = {
            "email": email,
            "password": password
        }
        response = self.session.post(url, data=payload)
        print(f"Request URL: {url}, Response Status: {response.status_code}, Response: {response.text}")
        return response

    def delete_method_to_delete_user_account(self, email, password):
        url = f"{self.base_url}deleteAccount"
        payload = {
            "email": email,
            "password": password
        }
        response = self.session.delete(url, data=payload)
        print(f"Request URL: {url}, Response Status: {response.status_code}, Response: {response.text}")
        return response

    def put_method_to_update_user_account(self, name, email, password, title, birth_date, birth_month, birth_year,
                                    firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number):
        url = f"{self.base_url}updateAccount"
        payload = {
            "name": name,
            "email": email,
            "password": password,
            "title": title,
            "birth_date": birth_date,
            "birth_month": birth_month,
            "birth_year": birth_year,
            "firstname": firstname,
            "lastname": lastname,
            "company": company,
            "address1": address1,
            "address2": address2,
            "country": country,
            "zipcode": zipcode,
            "state": state,
            "city": city,
            "mobile_number": mobile_number
        }
        response = self.session.put(url, data=payload)
        print(f"Request URL: {url}, Response Status: {response.status_code}, Response: {response.text}")
        return response