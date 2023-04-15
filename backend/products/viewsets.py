from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #default

# class ProductGenericViewSet(
#         mixins.ListModelMixin,
#         mixins.RetrieveModelMixin,
#         viewsets.GenericViewSet):
#     '''
#     get -> list -> Queryset
#     get -> retrieve -> Product Instance Detail View 
#     '''
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk' # default

# product_list_view = ProductGenericViewSet.as_view({'get': 'list'})
# product_detail_view = ProductGenericViewSet.as_view({'get': 'retrieve'})
'''
These above to vars can be used in place of class based api views in our custom urls
By doing this we leverage Viewsets as views
'''
