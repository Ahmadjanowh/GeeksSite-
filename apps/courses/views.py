from django.shortcuts import render, get_object_or_404
from apps.courses.models import *
from django.views.generic.base import View


def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def course_detail(request,pk):
    course = get_object_or_404(Course,pk=pk)
    return render(request,'course.html', {'course': course})



