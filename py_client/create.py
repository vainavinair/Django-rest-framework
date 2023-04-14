import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    'title':'Speaker',
    'content':'this is a speaker',
    'price':18.99
}
get_response=requests.post(endpoint,data) 
print(get_response.json()) 