from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm, ArticleSearchForm

def upload_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contents:article_list')
    else:
        form = ArticleForm()
    return render(request, 'upload_article.html', {'form': form})

def article_list(request):
    articles = Article.objects.all().only('id', 'title')
    form = ArticleSearchForm(request.GET)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        author = form.cleaned_data.get('author')
        created_at = form.cleaned_data.get('created_at')

        if title:
            articles = articles.filter(title__icontains=title)
        if author:
            articles = articles.filter(author__icontains=author)
        if created_at:
            articles = articles.filter(created_at__date=created_at)

    return render(request, 'article_list.html', {'articles': articles, 'form': form})

def article_search(request):
    form = ArticleSearchForm(request.GET)
    articles = Article.objects.all()

    if form.is_valid():
        title = form.cleaned_data.get('title')
        author = form.cleaned_data.get('author')
        created_at = form.cleaned_data.get('created_at')

        if title:
            articles = articles.filter(title__icontains=title)
        if author:
            articles = articles.filter(author__icontains=author)
        if created_at:
            articles = articles.filter(created_at__date=created_at)

    return render(request, 'contents/article_search.html', {'articles': articles, 'form': form})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'article_detail.html', context)