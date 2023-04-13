import requests

endpoint = "http://httpbin.org/ip"
endpoint = "http://httpbin.org/anything"

get_response=requests.get(endpoint) #It will emulate the requests a client would make

print(get_response.text) #prints the resource in text(json) obtained from the request made earlier

print(get_response.json()) #prints the resource in python dict obtained from the request made earlier

get_response=requests.get(endpoint, json={'query':'Vanv'}) #Send data as 'data'
print(get_response.json()) #prints the resource and echos the data sent in 'data'

get_response=requests.get(endpoint, data={'query':'Vanv'}) #Send data as 'form'
print(get_response.json()) #prints the resource and echos the data sent in 'form'

get_response=requests.get(endpoint, data={'query':'Vanv'})
print(get_response.status_code) #prints the status code of the requests

