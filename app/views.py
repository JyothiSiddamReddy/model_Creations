from django.shortcuts import render

# Create your views here.
from app.models import *
def topics_display(request):
    TLO=Topic.objects.all()
    d={'topics':TLO}
    return render(request,'topics_display.html',d)


def webpage_display(request):
    WLO=Webpage.objects.all()
    d={'WO':WLO}
    return render(request,'webpage_display.html',d)



def access(request):
    ALO=AccessRecord.objects.all()
    d={'access':ALO}
    return render(request,'access.html',d)





def insert_topic(request):
    tn=input('Enter the topic name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    TLO=Topic.objects.all()
    d={'topics':TLO}
    return render(request,'topics_display.html',d)



def insert_webpage(request):
    tn=input('Enter the topic name: ')
    n=input('Enter name: ')
    u=input('Enter url: ')
    TO=Topic.objects.get(topic_name=tn)
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    WLO=Webpage.objects.all()
    d={'WO':WLO}
    return render(request,'webpage_display.html',d)





def insert_access(request):
    pk=int(input('Enter the pk value of webpage: '))
    a=input('Enter authorname: ')
    d=input('Enter date: ')
    PK=Webpage.objects.get(pk=pk)
    AO=AccessRecord.objects.get_or_create(name=PK,author=a,date=d)[0]
    AO.save()
    ALO=AccessRecord.objects.all()
    d={'access':ALO}
    return render(request,'access.html',d)













