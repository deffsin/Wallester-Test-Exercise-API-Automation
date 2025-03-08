import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import post_to_search_product
from config.logging import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_post_to_search_product(api_client):
    search_query = "tshirt"
    response_data = post_to_search_product(api_client, search_query, expected_status_code=200)

    assert "products" in response_data, "Response does not contain 'products' field"
    assert isinstance(response_data["products"], list), "Products should be a list"
    assert len(response_data["products"]) > 0, "Products list is empty"

    for product in response_data["products"]:
        assert "category" in product, "Product category is missing"
        assert isinstance(product["category"], dict), f"Product category is not a dictionary: {product['category']}"

        assert "category" in product["category"], "Category field is missing in product category"
        category_name = product["category"]["category"]

        assert category_name.lower() == "tshirts", (
            f"Product ID {product['id']} has incorrect category: {category_name}"
        )

    logger.info(f"POST to searchProduct response: {response_data}")