import requests
from getpass import getpass


endpoint = "http://localhost:8000/api/auth/"
username = input("Enter your username: \n")
password = getpass("Enter your password: \n")

auth_resposne = requests.post(endpoint, json={'username':username ,'password': password})
print(auth_resposne.json()) 

if auth_resposne.status_code == 200:
    token = auth_resposne.json()['token']
    headers = {
        'Authorization': f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/"
    get_response=requests.get(endpoint, headers=headers) 
    # print(get_response.json()) 
    data = get_response.json()
    next_url = data['next']
    results = data["results"]
    print("next_url: ",next_url)
    print("results: ",results)
    # if next_url is not None:
    #     get_response = requests.get(endpoint,headers=headers)
    # print()