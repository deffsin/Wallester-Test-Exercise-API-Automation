import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import delete_method_to_delete_user_account
from config.logging import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_delete_method_to_delete_user_account(api_client):
    email = "deffsinco@gmail.com"
    password = "qwerty"
    response_data = delete_method_to_delete_user_account(api_client, email=email, password=password, expected_status_code=200)

    assert "message" in response_data, "Response does not contain 'message' field"
    assert response_data["message"], "Response 'message' field is empty"

    expected_message = "Account deleted!"
    assert response_data.get("message") == expected_message, (
        f"Unexpected response message: {response_data.get('message')}"
    )

    expected_keys = {"responseCode", "message"}
    assert set(response_data.keys()) == expected_keys, f"Unexpected fields in response: {response_data.keys()}"

    logger.info(f"DELETE method to delete user account response: {response_data}")
