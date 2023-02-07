import requests


def test_api_response_mockend():
    url = "https://mockend.com/Muntasir101/API_Automation_Python/posts"

    payload = {
        "body": "Hello from Python",
        "category": "three",
        "cover": "https://picsum.photos/seed/62740/1920/270",
        "createdAt": "2016-02-08T08:12:09Z",
        "id": 1,
        "title": "Python API",
        "views": 647
    }

    response = requests.post(url, data=payload)

    if response.status_code == 201:
        print("Successfully created user")
    else:
        print("Failed to create user, status code:", response.status_code)
