from django.urls import path

from app1.views import *


urlpatterns=[
    path('temp1/', temp1, name='temp1'),
]