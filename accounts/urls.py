
from django.urls import path

from . import views

urlpatterns = [
    #path('', views.login, name='login'),
    path('', views.register, name='register'),
    #path('', views.logout, name='logout'),
    
]