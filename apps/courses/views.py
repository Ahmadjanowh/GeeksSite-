from django.shortcuts import render
from apps.courses.models import *

# Create your views here.
def courses(request):
    courses = Courses.objects.all()
    return render(request,'courses.html',locals())
