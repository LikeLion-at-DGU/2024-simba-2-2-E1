from django.shortcuts import render, redirect, get_object_or_404
from .models import Varsity
# Create your views here.

def startpage(request):
    return render(request, 'main/startpage.html')

def mainpage(request):
    varsitys= Varsity.objects.all()
    return render(request,'main/mainpage.html', {'varsitys': varsitys})

def custompage(request):
    return render(request, 'main/custompage.html')

def varsity(request):
    varsity = Varsity(
        college=request.POST['college'],
        major=request.POST['major'],
        image_front=request.FILES.get('image_front'),
        image_back=request.FILES.get('image_back')
    )
    varsity.save()
    return redirect('mainpage')

