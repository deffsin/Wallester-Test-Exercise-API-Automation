import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import put_method_to_update_user_account
from config.logging import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_put_method_to_update_user_account(api_client):

    response_data = put_method_to_update_user_account(
        api_client,
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
        mobile_number="555555",
        expected_status_code=200
    )

    assert "message" in response_data, "Response does not contain 'message' field"
    assert response_data["message"], "Response 'message' field is empty"

    expected_message = "User updated!"
    assert response_data.get("message") == expected_message, (
        f"Unexpected response message: {response_data.get('message')}"
    )

    expected_keys = {"responseCode", "message"}
    assert set(response_data.keys()) == expected_keys, f"Unexpected fields in response: {response_data.keys()}"

    logger.info(f"PUT method to update user account response: {response_data}")
