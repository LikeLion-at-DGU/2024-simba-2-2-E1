from django.urls import path
from main import views

app_name='main'
urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('custom/',views.custompage,name='custompage')
]

