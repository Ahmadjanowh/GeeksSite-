from django.shortcuts import render
from apps.geekspro.models import *

# Create your views here.
def geekspro(request):
    settings = Settings.objects.latest('id')
    statistics = StatisticGeekspro.objects.all()
    howgeekspro = HowGeeksPro.objects.all()
    faq = GeeksproFAQ.objects.all()
    partners = Partners.objects.all()

    return render(request,'geekspro.html',locals())
