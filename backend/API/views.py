from django.shortcuts import render
from django.http import JsonResponse
import json

def api_home(request,*args,**kwrags):
    # request -> HttpRequest -> Django
    # request.body
    print(request.GET) #url params
    body = request.body #byte string of JSON data
    data={}
    # try block because body may not have data
    try:
        data=json.loads(body)
    except:
        pass
    print(data.keys())
    # data['headers']=request.headers #request.META but this is not serializable so we convert it to a dict
    # print(request.headers)
    data['params']= dict(request.GET)
    data['headers']= dict(request.headers) 
    data['content_type']= request.content_type
    return JsonResponse(data)

