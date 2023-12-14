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