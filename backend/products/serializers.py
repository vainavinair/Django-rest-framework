from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title, unique_title, validate_title_no_hello

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True) 
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field='pk')
    # email = serializers.EmailField(write_only=True) #wont show up on read operations
    title = serializers.CharField(validators=[validate_title, validate_title_no_hello, unique_title])
    class Meta:
        model = Product
        fields = [
            # 'user',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    # def validate_title(self, value): #validate_<fieldname>
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a products name")
    #     return value

    # def create(self, validated_data): 
    #     # email = validated_data.pop('email')  #this can be ran aslo in views.perform_create()
    #     return super().create(validated_data)
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')  
    #     return super().update(instance, validated_data)


    def get_edit_url(self, obj):
        # return f"/api/products/{obj.pk}"
        request = self.context.get('request') #self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={'pk':obj.pk}, request=request)

    def get_my_discount(self,obj):
        # try:
        #     return obj.get_discount()
        # except:
        #     return None
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return None
        return obj.get_discount()