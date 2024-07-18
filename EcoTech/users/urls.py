from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'users'

urlpatterns = [
    path('signup/',  signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('password_forgot', password_forgot_view, name='password_forgot'),
    path('security_questions', security_questions_view, name='security_questions'),
    path('password_reset/', password_reset_view, name='password_reset'),
    path('password_reset_done', password_reset_done_view, name='password_reset_done'),
]
