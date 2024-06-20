from django.urls import path
from .views import *

app_name='main'
urlpatterns = [
    path('', startpage, name='startpage'),
    path('main/', mainpage, name='mainpage'),
    path('custom/',custompage,name='custompage'),
    path('design/', selectpage, name='selectpage',)
]

