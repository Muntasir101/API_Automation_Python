import requests

url = "https://mockend.com/Muntasir101/API_Automation_Python/posts"

payload = {"username": "john", "email": "john@example.com"}

response = requests.post(url, data=payload)

if response.status_code == 201:
    print("Successfully created user")
else:
    print("Failed to create user, status code:", response.status_code)