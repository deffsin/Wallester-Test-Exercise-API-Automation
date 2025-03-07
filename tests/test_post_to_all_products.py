import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import post_to_all_products
from config.logging import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_post_to_all_products(api_client):
    response_data = post_to_all_products(api_client, expected_status_code=405)

    logger.info(f".....: {response_data}")