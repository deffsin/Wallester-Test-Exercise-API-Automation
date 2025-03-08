import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import delete_to_verify_login
from config.logging import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_delete_to_verify_login(api_client):

    response_data = delete_to_verify_login(
        api_client, expected_status_code=405
    )

    assert "message" in response_data, "Response does not contain 'message' field"
    assert response_data["message"], "Response 'message' field is empty"

    expected_message = "This request method is not supported."
    assert response_data["message"] == expected_message, (
        f"Unexpected response message: {response_data['message']}"
    )

    expected_keys = {"responseCode", "message"}
    assert set(response_data.keys()) == expected_keys, f"Unexpected fields in response: {response_data.keys()}"

    logger.info(f"DELETE to verifyLogin response: {response_data}")