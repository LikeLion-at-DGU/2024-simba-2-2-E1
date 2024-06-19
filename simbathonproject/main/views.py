from django.shortcuts import render, redirect, get_object_or_404
from .models import Varsity
# Create your views here.
def mainpage(request):
    return render(request,'main/mainpage.html')