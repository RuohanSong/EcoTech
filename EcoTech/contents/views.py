from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import *
from .forms import *

@login_required(login_url='users:login')
def upload_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.uploaded_by = request.user
            article.save()
            return redirect('contents:article_list')
    else:
        form = ArticleForm()
    return render(request, 'upload_article.html', {'form': form})

def article_list(request):
    articles = Article.objects.all().only('id', 'title').order_by('-created_at')
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
    comments = article.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
            # messages.success(request, 'Your comment has been added.')
            return redirect('contents:article_detail', pk=article.pk)
    else:
        comment_form = CommentForm()

    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'article_detail.html', context)

@login_required(login_url='users:login')
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('contents:article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'edit_article.html', {'form': form, 'article': article})

@login_required(login_url='users:login')
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('contents:article_list')
    return render(request, 'confirm_delete.html', {'article': article})

@login_required(login_url='users:login')
def confirm_delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return render(request, 'contents/delete_article.html')
    return render(request, 'contents/confirm_delete.html', {'article': article})


