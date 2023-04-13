from django.shortcuts import render
from django.http import JsonResponse

def api_home(request,*args,**kwrags):
    return JsonResponse({"message":"It works!"})

