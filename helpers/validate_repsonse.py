from config.logging import logger
import pytest

def validate_response(response, expected_status):
    if response.status_code != expected_status:
        logger.error(f"Unexpected status code: {response.status_code}")
        logger.error(f"Request URL: {response.url}")
        logger.error(f"Response Body: {response.text}")
        pytest.fail(f"Test failed due to unexpected status code: {response.status_code}")

    assert response.status_code == expected_status, f"Unexpected status code: {response.status_code}"

    try:
        return response.json()
    except ValueError:
        pytest.fail("Response body isn't valid JSON.")