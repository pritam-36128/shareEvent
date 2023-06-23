from django.contrib import admin
from django.urls import path
from . import views


#  router 
urlpatterns = [
    path('', views.home, name='home'),
    path('domain/share/<str:eventID>/', views.shareEvent, name='shareEvent')
]

