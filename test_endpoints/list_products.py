"""
this is like a prototopye of how the frontend 
will be fetching data from the backend 
using the requests pacage in python

"""
import requests
from auth_token.get_token import get_token
from getpass import getpass


endpoint="http://127.0.0.1:8000/api/v2/products/list"
data={
    "username":input("your username: "), #use kibo as username
    "password": getpass()  #password is 123
}
token=get_token(data)

headers={
    "Content-Type":"application/json",
    "Authorization":f"Bearer {token}"
}

response=requests.get(endpoint, headers=headers)
print(response.json())

# Ensure the server is running on a different terminal for it to work

