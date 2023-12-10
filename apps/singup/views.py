from django.shortcuts import render,redirect
from .models import *
from django.views.generic.base import View
from apps.base.views import index
# Create your views here.


def get(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        course = request.POST.get('course')
        CoursPost.objects.create(name=name,phone=phone,email=email,cours=course)
        return redirect('index')
    select = SelectCourses.objects.all()  
    return render(request,'postcourse.html',locals())

def junoirget(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        course = request.POST.get('course')
        GeeksJuniorCoursPost.objects.create(name=name,phone=phone,email=email,cours=course)
        return redirect('index')
    juniorselect = JuniorSelectCourses.objects.all()  
    return render(request,'postdes.html',locals())


def geeksproget(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        direction = request.POST.get('direction')
        learning = request.POST.get('learning')
        GeeksProPost.objects.create(name=name,phone=phone,email=email,direction=direction,learning=learning)
        return redirect('index')
    geekspro_directions = GeeksProdirections.objects.all()
    return render(request,'postgeekspro.html',locals())