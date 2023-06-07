from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.contrib.auth import authenticate

from .models import User, Token
from .serializers import UserCreateSerializer
# Create your views here.
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer





"""create user api """
class UserCreateView(ViewSet):
    # the user objects
    queryset=User.objects.all()
    serializer=UserCreateSerializer

    # post create method- to create user
    def create(self, request):
        serializer=self.serializer(data=request.data, context={'request':request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TokenObtainView(ViewSet):
    serializer_class = TokenObtainPairSerializer
    permission_classes = (permissions.AllowAny,)

    def create_token(self, request):
        username=request.data.get('username')
        password=request.data.get('password')
        print(password)

        user=User.objects.filter(username=username)
        if user.exists():
           user=user.first()
           if user.check_password(password):
                refresh=RefreshToken.for_user(user)
                response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                }
                return Response(response_data)
           else:
               return Response({
                   "error": "password dont match!"
               })
        else:
            return Response({
                "error": "user does not exist"
            })

