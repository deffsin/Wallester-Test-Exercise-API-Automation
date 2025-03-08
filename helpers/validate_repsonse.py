from config.logging import logger
import pytest

def validate_response(response, expected_status):
    response_json = {}

    try:
        response_json = response.json()
    except ValueError:
        pytest.fail("Response body isn't valid JSON.")

    if response.status_code != expected_status:
        logger.warning(
            f"Unexpected HTTP status: {response.status_code}. Expected: {expected_status}, "
            f"but responseCode in JSON: {response_json.get('responseCode')}"
        )

    if response_json.get("responseCode") != expected_status:
        pytest.fail(
            f"Test failed: expected responseCode {expected_status}, "
            f"but got {response_json.get('responseCode')}"
        )

    return response_json
