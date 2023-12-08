from django.shortcuts import render
from apps.about.models import * 

# Create your views here.
def about(request):
    settings = Settings.objects.latest('id')
    history = HistoryCreated.objects.all()
    ourvalues = OurValues.objects.all()
    princiles = Principles_work.objects.all()
    team = Team.objects.all()


    return render(request,'about.html',locals())