from helpers.validate_repsonse import validate_response

def get_all_products(api_client):
    response = api_client.get_all_products()
    return validate_response(response)