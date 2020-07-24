from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
from django.core.paginator import Paginator

def article_list(request):
    articles = Article.objects.all().order_by('date')
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'app/article_list.html', {'page_obj': page})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'app/article_detail.html', {'article': article})

@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            instance.tags.set(form.cleaned_data['tags'])
            return redirect('article:list')
    else:
        form = forms.CreateArticle
    return render(request, 'app/article_create.html', {'form': form})

def tag_create(request):
    if request.method == 'POST':
        form = forms.CreateTag(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('article:list')
    else:
        form = forms.CreateTag
    return render(request, 'app/article_create.html', {'form': form})