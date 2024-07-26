# contents/urls.py
from django.urls import path
from . import views

app_name = 'contents'

urlpatterns = [
    path('upload/', views.upload_article, name='upload_article'),
    path('articles/', views.article_list, name='article_list'),
    path('search/', views.article_search, name='article_search'),
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/<int:pk>/edit/', views.edit_article, name='edit_article'),
    path('article/<int:pk>/delete/', views.delete_article, name='delete_article'),
    path('article/<int:pk>/confirm_delete/', views.confirm_delete_article, name='confirm_delete_article'),
]