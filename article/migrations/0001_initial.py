# Generated by Django 2.1.3 on 2019-01-09 21:55

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık :')),
                ('content', ckeditor.fields.RichTextField(verbose_name='İçerik :')),
                ('image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Eklenecek dosyayı seçiniz :')),
                ('slug', models.SlugField(editable=False, max_length=60, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Yayinlanma Tarihi :')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanici Adi :')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=50, verbose_name='Kullanıcı Adı :')),
                ('comment_content', models.TextField(verbose_name='Yorum :')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.Article', verbose_name='Makale')),
            ],
            options={
                'ordering': ['-comment_date'],
            },
        ),
    ]
