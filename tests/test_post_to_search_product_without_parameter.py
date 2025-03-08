import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import post_to_search_product_without_parameter
from config.logging import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_post_to_search_product_without_parameter(api_client):
    response_data = post_to_search_product_without_parameter(api_client, expected_status_code=400)

    assert "message" in response_data, "Response does not contain 'message' field"

    expected_message = "Bad request, search_product parameter is missing in POST request."
    assert response_data["message"] == expected_message, (
        f"Unexpected response message: {response_data['message']}"
    )

    logger.info(f"POST to searchProduct without param response: {response_data}")
