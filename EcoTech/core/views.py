from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import random
from contents.models import Article, Comment
from users.models import Member


# Home page view- will load the default landing page
def home_view(request):
    articles = list(Article.objects.all())  # Convert the queryset to a list
    random.shuffle(articles)  # Shuffle the list

    # Ensure there are at least three articles
    random_article_1 = articles[0] if len(articles) > 0 else None
    random_article_2 = articles[1] if len(articles) > 1 else None
    random_article_3 = articles[2] if len(articles) > 2 else None

    daily_visits = request.COOKIES.get('daily_visits', 0)
    num_article = Article.objects.count()
    num_member = Member.objects.count()
    num_comment = Comment.objects.count()

    context = {
        'random_article_1': random_article_1,
        'random_article_2': random_article_2,
        'random_article_3': random_article_3,
        'daily_visits': daily_visits,
        'num_comment': num_comment,
        'num_article': num_article,
        'num_member': num_member,
    }

    return render(request, 'core/home.html', context)


#About Us view- Will load the page for About Us
def about_view(request):
    return render(request, 'core/about.html')


def faq_view(request):
    return render(request, 'core/FAQ.html')


def contact_view(request):
    return render(request, 'core/contact.html')
