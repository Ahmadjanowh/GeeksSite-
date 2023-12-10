from django.shortcuts import render
from apps.base.models import *
from apps.courses.models import Course
from apps.courses.views import *
# Create your views here.

def index(requests):
    settings = Settings.objects.latest('id')
    howareyou = HowAreYou.objects.all()
    larning_geeks = LearningGeeks.objects.all()
    geeksint = GeeksInt.objects.all()
    geeks_online = GeeksOnline.objects.latest('id')
    students = Students.objects.all()
    bishkek =  Bishkek.objects.latest('id')
    osh = Osh.objects.latest('id')
    kara_balta = KaraBalta.objects.latest('id')
    st_projects = StudentsProject.objects.all()
    courses = Course.objects.all()

    return render(requests,'index.html',locals())
def course_detail(request,pk):
    course = get_object_or_404(Course,pk=pk)
    return render(request,'course.html', {'course': course})