from django.urls import path
from . import views as product_views

urlpatterns = [
    path('<int:pk>/', product_views.ProductDetailAPIView.as_view(), name='product-details'),
    path('', product_views.ProductListCreateAPIView.as_view(), name='product-details'),
]