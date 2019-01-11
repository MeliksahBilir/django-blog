from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", verbose_name="Kullanici Adi :", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Başlık :", max_length=50)
    content = RichTextField(verbose_name="İçerik :")
    image = models.FileField(blank=True, null=True, verbose_name='Eklenecek dosyayı seçiniz :')
    slug = models.SlugField(unique=True, editable=False, max_length=60)
    created_date = models.DateTimeField(verbose_name="Yayinlanma Tarihi :", auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı','i'))
        unique_slug = slug
        counter = 1 
        while Article.objects.filter(slug = unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Article, self).save(args, **kwargs)
    
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name = 'Makale', related_name = 'comments')
    comment_author = models.CharField(max_length = 50, verbose_name = 'Kullanıcı Adı :')
    comment_content = models.TextField(verbose_name = 'Yorum :')
    comment_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
