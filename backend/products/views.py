from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from django.shortcuts import get_object_or_404
# from django.http import Http404

from .models import Product
from .serializers import ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    def perform_destroy(self,instance):
        #
        super().perform_destroy(instance)
    


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

class ProductListAPIView(generics.ListAPIView):
    '''
    Not gonna use
    '''

# function based view
# @api_view(["GET","POST"])
# def product_alt_view(request, pk=None, *args, **kwrags):
#     method = request.method

#     if method == "GET":
#         #Detail view
#         if pk is not None:
#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(obj).data
#             return Response(data)
#         #listview
#         queryset = Product.objects.all()
#         data = ProductSerializer(queryset,many=True).data
#         return Response(data)
    
#     if method == "POST":
#         serializer= ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True): # raise excpetion gives exact reason for error
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#         return Response(serializer.data)

    