from django.urls import path
from app3.views import *

urlpatterns=[
    path('temp3/', temp3, name='temp3')
]