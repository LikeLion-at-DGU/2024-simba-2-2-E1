from django.shortcuts import render
from .models import Varsity
# Create your views here.
def mainpage(request):
    return render(request,'main/mainpage.html')
def custompage(request):
    return render(request,'main/custompage.html')
def designpage(request):
    return render(request,'design/select_page.html')
