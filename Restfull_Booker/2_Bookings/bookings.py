import requests



def test_bookings_all_IDS():
    location = 'London'
    url = "https://restful-booker.herokuapp.com/booking"
    response = requests.get(url)
    print(response.status_code)
    # print(response.headers)
    print(response.text)


def test_bookings_get_specific_ID():
    # Need to update this code
    payload = {
        "token": "9d23a7742641a22"
    }
    url = "https://restful-booker.herokuapp.com/bookings/771"
    response = requests.get(url, data=payload)
    print(response.status_code)
    print(response.text)


def test_bookings_filter_firstName():
    # Need to update this code
    firstname = 'London'
    url = "https://restful-booker.herokuapp.com/booking"
    response = requests.get(url)
    print(response.status_code)
    # print(response.headers)
    print(response.text)
