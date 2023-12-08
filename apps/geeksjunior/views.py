from django.shortcuts import render
from apps.geeksjunior.models import *

# Create your views here.
def geeksjunior(request):
    settings = Settings.objects.latest('id')
    statistic = Statistic.objects.all()
    howjunior = HowJunior.objects.all()
    courses = GeekaJuniorCourses.objects.all()
    free_lesson = FreLesson.objects.latest('id')
    return render(request,'geeksjunior.html',locals())