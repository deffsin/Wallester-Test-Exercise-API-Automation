import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import put_to_all_brands
from config.logging import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_put_to_all_brands(api_client):
    response_data = put_to_all_brands(api_client, expected_status_code=405)

    assert "message" in response_data, "Response does not contain 'message' field"

    expected_message = "This request method is not supported."
    assert response_data["message"] == expected_message, (
        f"Unexpected response message: {response_data['message']}"
    )

    logger.info(f"PUT to brandsList response: {response_data}")