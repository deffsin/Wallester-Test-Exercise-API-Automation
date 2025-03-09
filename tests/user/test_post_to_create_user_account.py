import pytest
from mimesis import Person, Address
from mimesis.locales import Locale
from helpers.api_client import APIClient
from helpers.api_helpers import post_to_create_user_account
from config.logging import logger

person = Person(Locale.EN)
address = Address(Locale.EN)

@pytest.fixture
def api_client():
    return APIClient()

def generate_account_body():
    account = {
        "name": person.first_name(),
        "email": person.email(),
        "password": person.password(),
        "title": "Mr",
        "birth_date": "04",
        "birth_month": "09",
        "birth_year": "2000",
        "firstname": person.first_name(),
        "lastname": person.last_name(),
        "company": "Wallester",
        "address1": address.address(),
        "address2": "",
        "country": address.country(),
        "zipcode": address.postal_code(),
        "state": address.state(),
        "city": address.city(),
        "mobile_number": person.telephone()
    }

    log_created_account(person.email(), person.password())
    return account

def log_created_account(email, password):
    with open("created_accounts.txt", "a") as f:
        f.write(f"Email: {email}, Password: {password}\n")

def test_post_to_create_user_account(api_client):
    payload = generate_account_body()

    response_data = post_to_create_user_account(api_client, **payload, expected_status_code=201)

    assert "message" in response_data, "Response does not contain 'message' field"
    assert response_data["message"], "Response 'message' field is empty"

    expected_message = "User created!"
    assert response_data.get("message") == expected_message, (
        f"Unexpected response message: {response_data.get('message')}"
    )

    expected_keys = {"responseCode", "message"}
    assert set(response_data.keys()) == expected_keys, f"Unexpected fields in response: {response_data.keys()}"

    logger.info(f"POST to createAccount response: {response_data}")