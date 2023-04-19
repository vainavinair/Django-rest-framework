from django.urls import path
from .views import SearchListNewView

urlpatterns = [
    path('', SearchListNewView.as_view(), name='search'),
]