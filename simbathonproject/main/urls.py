from django.urls import path
from main import views

app_name='main'
urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('custom/',views.custompage,name='custompage'),
    path('design/', views.designpage,name='design_start_page')
]

