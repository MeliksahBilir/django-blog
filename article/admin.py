from django.contrib import admin

from .models import Article, Comment

# Register your models here.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = Article

    list_display = ['slug', 'author', 'created_date']    
    
    list_display_links = ['slug', 'created_date']
    
    search_fields = ['slug', 'content']

    list_filter = ['created_date']