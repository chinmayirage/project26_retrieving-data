from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topics(request):
    QST=topic.objects.all()
    d={'topics':QST}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSW=webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)
    
def display_Accessrecords(request):
    QSA=Accessrecords.objects.all()
    d={'Accessrecords':QSA}
    return render(request,'display_Accessrecords.html',d)
    