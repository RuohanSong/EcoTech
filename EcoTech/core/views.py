import mimetypes

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import random
from contents.models import Article, Comment
from users.models import Member
from .utils import increment_visits


# Home page view- will load the default landing page
def home_view(request):
    # Filter articles to only include those with images
    articles_with_images = [
        article for article in Article.objects.all()
        if article.document and mimetypes.guess_type(article.document.url)[0].startswith('image')
    ]

    random.shuffle(articles_with_images)  # Shuffle the list

    # Ensure there are at least three articles
    random_article_1 = articles_with_images[0] if len(articles_with_images) > 0 else None
    random_article_2 = articles_with_images[1] if len(articles_with_images) > 1 else None
    random_article_3 = articles_with_images[2] if len(articles_with_images) > 2 else None

    # Check if session key exists, if not create new session
    if not request.session.session_key:
        request.session.create()

    # Check if the visit is already counted in the session
    if 'visit_counted' not in request.session:
        # Increment the total visit count
        total_visits = increment_visits()
        request.session['visit_counted'] = True
    else:
        total_visits = increment_visits()

    # Get the session count for today's visit
    visits_today = request.session.get('daily_visits', 0)
    num_article = Article.objects.count()
    num_member = Member.objects.count()
    num_comment = Comment.objects.count()

    context = {
        'random_article_1': random_article_1,
        'random_article_2': random_article_2,
        'random_article_3': random_article_3,
        'total_visits': total_visits,
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
