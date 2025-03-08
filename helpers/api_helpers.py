from helpers.validate_repsonse import validate_response

def get_all_products(api_client, expected_status_code):
    response = api_client.get_all_products()
    return validate_response(response, expected_status_code)

def post_to_all_products(api_client, expected_status_code):
    response = api_client.post_to_all_products()
    return validate_response(response, expected_status_code)

def get_all_brands(api_client, expected_status_code):
    response = api_client.get_all_brands()
    return validate_response(response, expected_status_code)

def put_to_all_brands(api_client, expected_status_code):
    response = api_client.put_to_all_brands()
    return validate_response(response, expected_status_code)

def post_to_search_product(api_client, search_product, expected_status_code):
    response = api_client.post_to_search_product(search_product)
    return validate_response(response, expected_status_code)