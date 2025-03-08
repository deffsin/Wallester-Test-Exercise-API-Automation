import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import get_user_account_detail_by_email
from config.logging import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_get_user_account_detail_by_email(api_client):
    email = "deffsinco@gmail.com"
    response_data = get_user_account_detail_by_email(api_client, email, expected_status_code=200)

    assert "user" in response_data, "Response does not contain 'user' field"
    user = response_data["user"]

    assert "email" in user, "User email is missing"
    assert isinstance(user["email"], str), "Email is not a string"
    assert user["email"] == email, f"Unexpected email in response: {user['email']}"

    assert "id" in user, "User ID is missing"
    assert isinstance(user["id"], int), f"User ID is not an integer: {user['id']}"
    assert user["id"] > 0, f"User ID should be positive, but got {user['id']}"

    assert "name" in user, "User name is missing"
    assert isinstance(user["name"], str), "User name is not a string"
    assert len(user["name"]) > 0, "User name is empty"

    assert "first_name" in user, "First name is missing"
    assert isinstance(user["first_name"], str), "First name is not a string"
    assert len(user["first_name"]) > 0, "First name is empty"

    assert "last_name" in user, "Last name is missing"
    assert isinstance(user["last_name"], str), "Last name is not a string"
    assert len(user["last_name"]) > 0, "Last name is empty"

    assert "title" in user, "Title is missing"
    assert isinstance(user["title"], str), "Title is not a string"
    assert user["title"] in ["Mr", "Mrs", "Miss"], f"Unexpected title: {user['title']}"

    assert "birth_day" in user, "Birth day is missing"
    assert isinstance(user["birth_day"], str), "Birth day is not a string"
    assert user["birth_day"].isdigit(), "Birth day should be numeric"
    assert 1 <= int(user["birth_day"]) <= 31, f"Invalid birth day: {user['birth_day']}"

    assert "birth_month" in user, "Birth month is missing"
    assert isinstance(user["birth_month"], str), "Birth month is not a string"
    assert user["birth_month"].isdigit(), "Birth month should be numeric"
    assert 1 <= int(user["birth_month"]) <= 12, f"Invalid birth month: {user['birth_month']}"

    assert "birth_year" in user, "Birth year is missing"
    assert isinstance(user["birth_year"], str), "Birth year is not a string"
    assert user["birth_year"].isdigit(), "Birth year should be numeric"
    assert 1900 <= int(user["birth_year"]) <= 2024, f"Invalid birth year: {user['birth_year']}"

    assert "company" in user, "Company is missing"
    assert isinstance(user["company"], str), "Company is not a string"

    assert "address1" in user, "Address1 is missing"
    assert isinstance(user["address1"], str), "Address1 is not a string"
    assert len(user["address1"]) > 0, "Address1 is empty"

    assert "address2" in user, "Address2 is missing"
    assert isinstance(user["address2"], str), "Address2 is not a string"

    assert "country" in user, "Country is missing"
    assert isinstance(user["country"], str), "Country is not a string"
    assert len(user["country"]) > 0, "Country is empty"

    assert "state" in user, "State is missing"
    assert isinstance(user["state"], str), "State is not a string"
    assert len(user["state"]) > 0, "State is empty"

    assert "city" in user, "City is missing"
    assert isinstance(user["city"], str), "City is not a string"
    assert len(user["city"]) > 0, "City is empty"

    assert "zipcode" in user, "Zipcode is missing"
    assert isinstance(user["zipcode"], str), "Zipcode is not a string"
    assert user["zipcode"].isdigit(), "Zipcode should be numeric"
    assert len(user["zipcode"]) >= 4, "Zipcode is too short"

    logger.info(f"User account details: {user}")