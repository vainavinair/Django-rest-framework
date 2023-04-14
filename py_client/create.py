import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    'title':'Speaker',
    'price':18.99
}
get_response=requests.post(endpoint,data) 
print(get_response.json()) 