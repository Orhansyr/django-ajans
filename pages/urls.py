
from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name="anasayfa"),
     path('services/', views.services, name="services"),
]