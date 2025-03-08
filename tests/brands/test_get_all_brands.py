import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import get_all_brands
from config.logging import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_get_all_brands(api_client):
    response_data = get_all_brands(api_client, expected_status_code=200)
    brands = response_data.get('brands', [])

    assert isinstance(brands, list), "Brands should be a list"
    assert len(brands) > 0, "Brands list is empty"
    assert len(brands) <= 150, "Too many brands returned"

    brands_ids = set()

    for brand in brands:
        assert "id" in brand, "Brand ID is missing"
        assert isinstance(brand["id"], int), f"Brand ID isn't an integer: {brand['id']}"
        assert brand["id"] > 0, f"Brand ID should be positive, but got: {brand['id']}"
        assert brand["id"] not in brands_ids, f"Duplicate brand ID was found: {brand['id']}"
        brands_ids.add(brand["id"])

        assert "brand" in brand, "Brand name is missing" # Brand name
        assert brand["brand"] is not None, f"Brand name is None for brand ID {brand['id']}"
        assert isinstance(brand["brand"], str), f"Brand name isn't a string: {brand['brand']}"
        assert len(brand["brand"]) > 0, "Brand name is empty"

    logger.info(f"Brands data: {brands}")