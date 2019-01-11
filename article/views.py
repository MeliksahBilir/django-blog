from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.template import Template, Context
from .forms import ArticleForm
from .models import Article, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def articles(request):
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(title__contains = query)
        paginator = Paginator(articles, 4)
        page = request.GET.get('page')
        articles = paginator.get_page(page)
        return render(request, 'articles.html', {'articles' : articles})

    articles = Article.objects.all()
    paginator = Paginator(articles, 4)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'articles.html', {'articles' : articles})

@login_required(login_url = 'user:login')
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        'articles' : articles
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url = 'user:login')
def detail(request, slug):
    article = get_object_or_404(Article, slug = slug)
    comments = article.comments.all()
    context = {
        'article' : article,
        'comments' : comments
    }
    return render(request, 'detail.html', context)

@login_required(login_url = 'user:login')
def update(request, slug):
    article = get_object_or_404(Article, slug = slug)
    form = ArticleForm(request.POST or None, request.FILES or None, instance = article)
    if form.is_valid():

        article = form.save(commit = False)
        article.author = request.user
        article.save()

        messages.success(request, 'Makale GÜncellendi...')
        return redirect('article:dashboard')

    context = {
        'form' : form
    }

    return render(request, 'update.html', context)

@login_required(login_url = 'user:login')
def delete(request, id):
    article = get_object_or_404(Article, id = id)
    article.delete()
    messages.success(request, 'Makaleniz Silindi...')
    # index disinda bir yere gitmek icin
    return redirect('article:dashboard')

@login_required(login_url = 'user:login')
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
       
        article = form.save(commit = False)
        article.author = request.user
        article.save()

        messages.success(request, 'Makale Oluşturuldu...')
        return redirect('article:dashboard')

    context = {'form' : form}
    return render(request, 'addarticle.html', context)

@login_required(login_url = 'user:login')
def addComment(request, slug):
    article = get_object_or_404(Article, slug = slug)

    if request.method == 'POST':
        comment_author = request.POST.get('comment_author')
        comment_content = request.POST.get('comment_content')
        
        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        # yorum yazilacak makaleyi id si cekip Comment model de foreign key ile baglama islemi
        newComment.article = article
        newComment.save()
        
    return redirect(reverse('article:detail', kwargs={'slug':slug}))

