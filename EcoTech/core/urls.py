from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('FAQ/', views.faq_view, name='faq'),
    path('signup/', views.signup_view, name='signup'),
]