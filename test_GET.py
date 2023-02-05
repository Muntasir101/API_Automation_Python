import requests
import pytest


def test_api_response():
    location = 'London'
    url = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&APPID=eb94d4c29e11529ba1d8a292dcdc4197"
    response = requests.get(url)
    print(response.status_code)
    print(response.headers)
    print(response.text)

    assert response.status_code == 200
    assert response.json()["name"] == location

    # assert static specific response
    assert response.json()["weather"] == [{'description': 'broken clouds',
                                           'icon': '04d',
                                           'id': 803,
                                           'main': 'Clouds'}]
    # assert dynamic response data type
    # step 1: find a specific value type from an API response
    # step 2: apply assertion for this response data type
    data_type = response.json()
    specific_value_temp = data_type["main"]["temp"]
    specific_value_feels_like = data_type["main"]["feels_like"]
    specific_value_temp_min = data_type["main"]["temp_min"]
    specific_value_temp_max = data_type["main"]["temp_max"]
    specific_value_pressure = data_type["main"]["pressure"]
    specific_value_humidity = data_type["main"]["humidity"]
    print(type(specific_value_temp))
    assert str(type(specific_value_temp)) == "<class 'float'>"
    assert str(type(specific_value_temp_min)) == "<class 'float'>"
    assert str(type(specific_value_temp_max)) == "<class 'float'>"
    assert str(type(specific_value_pressure)) == "<class 'int'>"
    assert str(type(specific_value_humidity)) == "<class 'int'>"

    # assert all key present or not on response
    # step 1: find all key from an API response
    # step 2: apply assertion for this
    data_keys = response.json()
    expected_all_keys = [
        'coord', 'weather', 'base', 'main',
        'visibility', 'wind', 'clouds', 'dt',
        'sys', 'timezone', 'id', 'name', 'cod']

    # assert all key present or not on response
    actual_all_keys = list(response.json().keys())
    print(actual_all_keys)

    assert expected_all_keys == actual_all_keys

    # assert specific key present or not on response
    specific_key = data_keys.get("main")
    assert specific_key is not None

