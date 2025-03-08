import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import post_to_create_user_account
from config.logging import logger

@pytest.fixture
def api_client():
    return APIClient()

def generate_account_body(name, email, password, title, birth_date, birth_month, birth_year,
                          firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number):
    return {
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

def test_post_to_create_user_account(api_client):
    payload = generate_account_body(
        name="Denis",
        email="deffsinco@gmail.com",
        password="qwerty",
        title="Mr",
        birth_date="04",
        birth_month="09",
        birth_year="2000", # 2024 limit
        firstname="Denis",
        lastname="S",
        company="Wallester",
        address1="Pikk 100",
        address2="",
        country="Estonia",
        zipcode="13000",
        state="Harjumaa",
        city="Tallinn",
        mobile_number="555555"
    )

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