import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import get_all_products
from config.logging import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_get_all_products(api_client):
    response_data = get_all_products(api_client)
    products = response_data.get('products', [])

    assert isinstance(products, list), "Products should be a list"
    assert len(products) > 0, "Products list is empty"
    assert len(products) <= 150, "Too many products returned" # produktov ne mojet bqt' bolwe 150

    products_ids = set() # dlja proverki dublikatov

    for product in products:
        assert "id" in product, "Product ID is missing"
        assert isinstance(product["id"], int), f"Product ID isn't an integer: {product['id']}"
        assert product["id"] not in products_ids, f"Duplicate product ID was found: {product['id']}"
        products_ids.add(product["id"])

        assert "name" in product, "Product name is missing"
        assert isinstance(product["name"], str), f"Product name isn't a string: {product['name']}"
        assert len(product["name"]) > 0, "Product name is empty"

        assert "price" in product, "Product price is missing"
        assert isinstance(product["price"], str), f"Product price isn't a string: {product['price']}"
        assert len(product["price"]) > 0, "Product price is empty"

        assert "brand" in product, "Product brand is missing"
        assert isinstance(product["brand"], str), f"Product brand isn't a string: {product['brand']}"
        assert len(product["brand"]) > 0, "Product brand is empty"

        category = product["category"]
        assert isinstance(category, dict), f"Product category isn't a dict: {category}"
        assert "usertype" in category, "usertype missing in category" # women/men
        assert isinstance(category["usertype"], dict), f"usertype isn't a dict: {category['usertype']}"
        assert "category" in category, "Category name missing" # Tshirts, hats and etc
        assert isinstance(category["category"], str), "Category name isn't a string"
        assert len(category["category"]) > 0, "Category name is empty"

    logger.info(f"Product data: {products}")