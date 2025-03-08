import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import post_to_all_products
from config.logging import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_post_to_all_products(api_client):
    response_data = post_to_all_products(api_client, expected_status_code=405)

    assert "message" in response_data, "Response does not contain 'message' field"

    expected_message = "This request method is not supported."
    assert response_data["message"] == expected_message, (
        f"Unexpected response message: {response_data['message']}"
    )

    logger.info(f"POST to productsList response: {response_data}")