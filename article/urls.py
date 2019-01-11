from django.contrib import admin
from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('addarticle/', views.addArticle, name = 'addarticle'),
    path('', views.articles, name = 'articles'),
    path('article/<slug:slug>', views.detail, name = 'detail'),
    path('update/<slug:slug>', views.update, name = 'update'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('comment/<slug:slug>', views.addComment, name = 'comment'),
]