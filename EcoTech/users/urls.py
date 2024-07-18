from django.urls import path
from django.contrib import admin
from .views import *

app_name = 'users'

urlpatterns = [
    path('signup/',  signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<str:username>/', view_profile, name='view_profile'),
    path('profile/<str:username>/edit/', edit_profile, name='edit_profile'),

]
