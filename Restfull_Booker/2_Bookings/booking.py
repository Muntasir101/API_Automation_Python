import requests


def test_bookings_get_all_IDs():
    url = "https://restful-booker.herokuapp.com/booking"
    response = requests.get(url)
    print(response.status_code)
    # print(response.headers)
    # print(response.text)


def test_bookings_get_specific_ID():
    url = "https://restful-booker.herokuapp.com/booking"
    response = requests.get(url)

    # Get specific booking id
    data_type = response.json()
    specific_id_retrieve = data_type[1]["bookingid"]
    print("specific_id_retrieve :" + str(specific_id_retrieve))

    headers_authorization = {
        "token": "67fad78b804a9e9"
    }
    url = "https://restful-booker.herokuapp.com/booking/" + str(specific_id_retrieve)
    response = requests.get(url, headers=headers_authorization)
    print(response.status_code)
    # print(response.text)

    # assert all key present or not on response
    # step 1: find all key from an API response
    # step 2: apply assertion for this
    data_keys = response.json()
    expected_all_keys = ['firstname', 'lastname', 'totalprice',
                         'depositpaid', 'bookingdates', 'additionalneeds']

    # assert all key present or not on response
    actual_all_keys = list(response.json().keys())
    print(actual_all_keys)

    assert expected_all_keys == actual_all_keys


def test_bookings_filter_by_firstName_and_lastname():
    # curl -i https://restful-booker.herokuapp.com/booking?firstname=sally&lastname=brown

    url = "https://restful-booker.herokuapp.com/booking"
    response = requests.get(url)

    # Get specific bookingID from response
    data_type = response.json()
    specific_id_retrieve = data_type[1]["bookingid"]
    print("specific_id_retrieve :" + str(specific_id_retrieve))

    headers_authorization = {
        "token": "67fad78b804a9e9"
    }
    url = "https://restful-booker.herokuapp.com/booking/" + str(specific_id_retrieve)
    response = requests.get(url, headers=headers_authorization)

    # Get specific firstname and lastname by using previous bookingID
    data_type = response.json()
    specific_firstname_retrieve = data_type["firstname"]
    specific_lastname_retrieve = data_type["lastname"]
    print("specific_firstname_retrieve :" + str(specific_firstname_retrieve))
    print("specific_lastname_retrieve :" + str(specific_lastname_retrieve))

    # Filter By firstname and lastname
    url = "https://restful-booker.herokuapp.com/booking?firstname="+specific_firstname_retrieve+"&lastname="+specific_lastname_retrieve
    response = requests.get(url, headers=headers_authorization)
    print(response.status_code)
    print(response.text)
