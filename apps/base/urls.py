from django.urls import path
from apps.base.views import *
from apps.courses.views import * 


urlpatterns = [
    path('',index,name='index'),
    path('<int:pk>/',course_detail, name='course_detail')

]