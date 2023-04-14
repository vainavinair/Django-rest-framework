import requests

endpoint = "http://localhost:8000/api/"

get_response=requests.post(endpoint,json={'title':'Toilet Paper'}) #Send data as 'data'
print(get_response.json()) #prints the resource and echos the data sent in 'form'

