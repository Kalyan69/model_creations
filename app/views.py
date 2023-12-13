from django.shortcuts import render

from app.models import *

# Create your views here.

def display_topics(request):
    QLOT=Topic.objects.all()
    D={'topics':QLOT}
    return render(request,'display_topics.html',context=D)


def display_webpage(request):
    QLOW=Webpage.objects.all()
    Q={'webpages':QLOW}
    return render(request,'display_webpage.html',Q)


def AcessRecord(request):
    QLOA=AcessRocord.objects.all()
    A={'AcessRecord':QLOA}
    return render(request,'AcessRecords.html',A)
