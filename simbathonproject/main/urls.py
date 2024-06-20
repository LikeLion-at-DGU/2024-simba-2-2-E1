from django.urls import path
from .views import *

app_name='main'
urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('custom/',custompage,name='custompage'),
    path('design/', designpage,name='design_start_page')
]

