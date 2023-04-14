from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view


from django.forms.models import model_to_dict

from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request,*args,**kwrags):
    '''
    DRF view
    '''
    # instance=Product.objects.all().order_by("?").first()
    # data=request.data
    serializer= ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({'invalid':'not good data'},status=400)

