from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm, ArticleSearchForm

def upload_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contents:article_list')
    else:
        form = ArticleForm()
    return render(request, 'upload_article.html', {'form': form})

def article_list(request):
    articles = Article.objects.all()
    form = ArticleSearchForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['title']:
            articles = articles.filter(title__icontains=form.cleaned_data['title'])
        if form.cleaned_data['author']:
            articles = articles.filter(author__icontains=form.cleaned_data['author'])
        if form.cleaned_data['created_at']:
            articles = articles.filter(created_at__date=form.cleaned_data['created_at'])
    return render(request, 'article_list.html', {'articles': articles, 'form': form})

def article_search(request):
    # Implement article search logic here
    # Example: filtering articles based on user input
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(title__icontains=query)
    else:
        articles = Article.objects.all()
    return render(request, 'contents/article_search.html', {'articles': articles})