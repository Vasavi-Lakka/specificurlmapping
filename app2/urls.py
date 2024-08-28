from django.urls import path
from app2.views import *

urlpatterns=[
    path('temp2/', temp2, name='temp2')
]