import requests

endpoint = "http://localhost:8000/api/"

get_response=requests.get(endpoint, params={"abc":123} ,json={'query':'Vanv'}) #Send data as 'data'
print(get_response.json()) #prints the resource and echos the data sent in 'form'

