from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request,'main/mainpage.html')


def custompage(request):
    return render(request,'main/custompage.html')