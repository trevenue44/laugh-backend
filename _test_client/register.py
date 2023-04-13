import requests

register_endpoint = "http://localhost:8000/api/accounts/register/"

# sending a post request to the endpoint with new user data.
response = requests.post(
    register_endpoint, data={"username": "trevenue44", "password": "mypassword"}
)
# displaying json reponse from the API
print(response.json())
