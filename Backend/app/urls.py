from django.urls import path
from .views import *

urlpatterns=[
    path('stulist/',stulist,name='stulist')
]