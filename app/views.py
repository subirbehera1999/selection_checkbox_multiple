from django.shortcuts import render
from app.models import *
# Create your views here.
def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=="POST":
        topic_name=request.POST['topic_name']
        name=request.POST['name']
        url=request.POST['url']
        TO=Topic.objects.get(topic_name=topic_name)

        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        QSWO=Webpage.objects.all()
        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)


    return render(request,'insert_webpage.html',d)

def select_display(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tnlist=request.POST.getlist('topic_name')

        QSWO=Webpage.objects.none()
        for topic_name in tnlist:
            QSWO=QSWO|Webpage.objects.filter(topic_name=topic_name)
        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)

    return render(request,'select_display.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    
    return render(request,'checkbox.html',d)