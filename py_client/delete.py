import requests

pid = input("What is the product if you want to delete: \n")

try:
    pid = int(pid)
except:
    pid = None
    print(f'{pid} is not a valid product id')

if pid:
    endpoint = f'http://localhost:8000/api/products/{pid}/delete'

get_response=requests.delete(endpoint) 
print(get_response.status_code,get_response.status_code==204) 

