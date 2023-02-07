import requests


def test_auth_valid():
    url = "https://restful-booker.herokuapp.com/auth"

    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Successfully Login.Status Code: " + str(response.status_code))
        print(response.text)
    else:
        print("Failed to Login.Status Code: " + str(response.status_code))

    # Get Token from Response
    get_response_value_token = response.json()['token']
    print(get_response_value_token)

    assert response.status_code == 200

    return get_response_value_token
