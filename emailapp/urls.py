from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('email', send_email, name='email'),
    path('', home, name='home'),
]
