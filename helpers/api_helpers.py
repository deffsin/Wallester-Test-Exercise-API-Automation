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

def post_to_search_product_without_parameter(api_client, expected_status_code):
    response = api_client.post_to_search_product_without_parameter()
    return validate_response(response, expected_status_code)

def post_to_verify_login_with_valid_details(api_client, email, password, expected_status_code):
    response = api_client.post_to_verify_login_with_valid_details(email, password)
    return validate_response(response, expected_status_code)

def post_to_create_user_account(api_client, name, email, password, title, birth_date, birth_month, birth_year,
                                firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number, expected_status_code):
    response = api_client.post_to_create_user_account(
        name=name,
        email=email,
        password=password,
        title=title,
        birth_date=birth_date,
        birth_month=birth_month,
        birth_year=birth_year,
        firstname=firstname,
        lastname=lastname,
        company=company,
        address1=address1,
        address2=address2,
        country=country,
        zipcode=zipcode,
        state=state,
        city=city,
        mobile_number=mobile_number
    )
    return validate_response(response, expected_status_code)

def post_to_verify_login_without_email_parameter(api_client, password, expected_status_code):
    response = api_client.post_to_verify_login_without_email_parameter(password)
    return validate_response(response, expected_status_code)

def delete_to_verify_login(api_client, expected_status_code):
    response = api_client.delete_to_verify_login()
    return validate_response(response, expected_status_code)