from django.contrib import admin
from django.urls import path
from . import views
# from .views import *
# ImportError: cannot import name 'views' from '__main__' (C:/Users/tymot/Desktop/weather app/env/Environemnt/the_weather/weather/views.py)


app_name = 'worker'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout')

]
