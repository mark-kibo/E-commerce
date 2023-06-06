import requests




def get_token(login_data):
    endpoint="http://127.0.0.1:8000/api/v1/token/"
    response=requests.post(endpoint, json=login_data)
    # print(response.json().get('access'))
    return response.json().get('access')
