from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product

from django.forms.models import model_to_dict



def api_home(request,*args,**kwrags):
    model_data=Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        #serialization: we are turning a model instance into a python dictionary
        # data['id']=model_data.id
        # data['title']=model_data.title
        # data['content']=model_data.content
        # data['price']=model_data.price

        # using model_to_dict()
        data = model_to_dict(model_data, fields=['title']) # field parameter if not specified send all fields.
    return JsonResponse(data)

