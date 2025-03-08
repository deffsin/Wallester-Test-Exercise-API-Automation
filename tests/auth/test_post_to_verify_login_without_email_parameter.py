import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import post_to_verify_login_without_email_parameter
from config.logging import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_post_to_verify_login_without_email_parameter(api_client):
    password = "qwerty"

    response_data = post_to_verify_login_without_email_parameter(
        api_client, password=password, expected_status_code=400
    )

    assert "message" in response_data, "Response does not contain 'message' field"
    assert response_data["message"], "Response 'message' field is empty"

    expected_message = "Bad request, email or password parameter is missing in POST request."
    assert response_data["message"] == expected_message, (
        f"Unexpected response message: {response_data['message']}"
    )

    expected_keys = {"responseCode", "message"}
    assert set(response_data.keys()) == expected_keys, f"Unexpected fields in response: {response_data.keys()}"

    logger.info(f"POST to verifyLogin without email parameter response: {response_data}")
