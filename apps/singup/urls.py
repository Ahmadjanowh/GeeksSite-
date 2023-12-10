from django.urls import path
from .views import *
urlpatterns = [
    path('courses_singup',get,name='courses_post'),
    path('geeksjunior_singup',junoirget,name='juniorpost'),
    path('geekspro_singup',geeksproget,name='geekspro_post')
]