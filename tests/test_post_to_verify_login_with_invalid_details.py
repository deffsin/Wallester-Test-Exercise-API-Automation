import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import post_to_verify_login_with_invalid_details
from config.logging import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_post_to_verify_login_with_invalid_details(api_client):
    email = "deffsinco@gmail.com"
    password = "invalidpass!" # qwerty is a valid pass

    response_data = post_to_verify_login_with_invalid_details(
        api_client, email=email, password=password, expected_status_code=404
    )

    assert "message" in response_data, "Response does not contain 'message' field"
    assert response_data["message"], "Response 'message' field is empty"

    expected_message = "User not found!"
    assert response_data["message"] == expected_message, (
        f"Unexpected response message: {response_data['message']}"
    )

    expected_keys = {"responseCode", "message"}
    assert set(response_data.keys()) == expected_keys, f"Unexpected fields in response: {response_data.keys()}"

    logger.info(f"POST to verifyLogin with invalid details response: {response_data}")
