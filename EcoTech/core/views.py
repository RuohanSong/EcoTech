from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


from contents.models import Article


# Home page view- will load the default landing page
def home_view(request):
    daily_visits = request.COOKIES.get('daily_visits', 0)
    # total_visits = request.COOKIES.get('total_visits', 0)

    num_article = Article.objects.count()
    context = {
        'daily_visits': daily_visits,
        # 'total_visits': total_visits,
        'num_article': num_article,
    }

    return render(request, 'core/home.html', context)


#About Us view- Will load the page for About Us
def about_view(request):
    return render(request, 'core/about.html')


def faq_view(request):
    return render(request, 'core/FAQ.html')


def contact_view(request):
    return render(request, 'core/contact.html')
