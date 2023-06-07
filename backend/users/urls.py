from django.urls import path
from .views import *

urlpatterns=[
    path('create-user', UserCreateView.as_view({'post': 'create'})),
]