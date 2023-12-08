from django.urls import path
from apps.about.views import *

urlpatterns = [
    path('',about,name='about')
]