from .models import Product
from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_id', 'name', 'price', 'description', 'image_url')