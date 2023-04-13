import requests

login_endpoint = "http://localhost:8000/api/accounts/login/"

# sending a post request to the endpoint with user details.
response = requests.post(
    login_endpoint, data={"username": "trevenue44", "password": "mypassword"}
)
# displaying json reponse from the API
print(response.json())


# print("=== checking for logged in state ===")

# logged_in_response = requests.get(login_endpoint)
# print(logged_in_response.json())
