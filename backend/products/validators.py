from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Product


def validate_title(value): #validate_<fieldname>
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a products name")
    return value


def validate_title_no_hello(value):
    if "hello" in value.lower():
           raise serializers.ValidationError("Hello is not allowed")
    return value

unique_title = UniqueValidator(queryset=Product.objects.all())
