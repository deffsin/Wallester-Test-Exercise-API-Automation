import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import post_to_create_user_account
from config.logging import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_post_to_create_user_account(api_client):

    response_data = post_to_create_user_account(
        api_client,
        name="Denis",
        email="dffsinco@gmail.com",
        password="qwerty",
        title="Mr",
        birth_date="04",
        birth_month="09",
        birth_year="2000",
        firstname="Denis",
        lastname="S",
        company="Wallester",
        address1="Pikk 100",
        address2="",
        country="Estonia",
        zipcode="13000",
        state="Harjumaa",
        city="Tallinn",
        mobile_number="555555",
        expected_status_code=201
    )

    assert "message" in response_data, "Response does not contain 'message' field"
    assert response_data["message"], "Response 'message' field is empty"

    expected_message = "User created!"
    assert response_data.get("message") == expected_message, (
        f"Unexpected response message: {response_data.get('message')}"
    )

    expected_keys = {"responseCode", "message"}
    assert set(response_data.keys()) == expected_keys, f"Unexpected fields in response: {response_data.keys()}"

    logger.info(f"POST to createAccount response: {response_data}")
