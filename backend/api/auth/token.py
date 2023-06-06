from rest_framework.authentication import TokenAuthentication as BaseAuth
from rest_framework_simplejwt.authentication import JWTAuthentication


class TokenAuthentication(JWTAuthentication):
    keyword="Bearer"