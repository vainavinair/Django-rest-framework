from django.urls import path
from . import views as product_views

urlpatterns = [
    path('<int:pk>/', product_views.ProductDetailAPIView.as_view(), name="product-detail"),
    path('<int:pk>/update', product_views.ProductUpdateAPIView.as_view(), name="product-edit"),
    path('<int:pk>/delete', product_views.ProductDeleteAPIView.as_view()),
    path('', product_views.ProductListCreateAPIView.as_view(), name="product-list"),
]