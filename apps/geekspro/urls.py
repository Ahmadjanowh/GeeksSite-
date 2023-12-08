from django.urls import path
from apps.geekspro.views import *

urlpatterns = [
    path('geekspro',geekspro,name='geekspro')
]