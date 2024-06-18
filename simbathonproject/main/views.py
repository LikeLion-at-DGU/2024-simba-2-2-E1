from django.shortcuts import render
from .models import Varsity
# Create your views here.
def mainpage(request):
    return render(request,'main/mainpage.html')

