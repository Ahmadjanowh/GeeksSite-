from django.urls import path
from apps.geeksjunior.views import *
urlpatterns = [
    path('',geeksjunior,name='geeksjunior')
]