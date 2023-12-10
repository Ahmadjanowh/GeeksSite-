from django.urls import path
from apps.courses.views  import *

urlpatterns = [
    path('',courses,name='courses'),
    path('<int:pk>/',course_detail, name='course_detail')
]