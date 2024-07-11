from django.urls import path
from django.contrib import admin
from .views import *

app_name = 'users'

urlpatterns = [
    path('signup/',  signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
