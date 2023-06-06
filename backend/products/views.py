from django.shortcuts import render
from rest_framework.generics import ListAPIView
from api.auth.token import TokenAuthentication

# models
from .models import Product
# serializers
from .serializers import ProductSerializer
# Create your views here.



class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes=[TokenAuthentication]
   
