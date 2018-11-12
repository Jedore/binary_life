# Create your models here.

from django.db import models
from django.utils import timezone


# Create your models here.


class ArticleType(models.Model):
    name = models.CharField(max_length=16, unique=True)
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)


class ArticleTags(models.Model):
    name = models.CharField(max_length=16, unique=True)
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)


class Article(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=1024, null=True, default=None)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)
    article_type = models.ForeignKey(ArticleType, related_name='articles', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(ArticleTags, related_name='articles')
    is_hide = models.BooleanField(default=False)
    page_view = models.PositiveIntegerField(default=0)
    unique_view = models.PositiveIntegerField(default=0)
    ip_view = models.PositiveIntegerField(default=0)
    author = models.CharField(max_length=16)


class ViewsRecord(models.Model):
    username = models.CharField(max_length=32)
    is_anonymous = models.BooleanField()
    is_superuser = models.BooleanField()
    scheme = models.CharField(max_length=16)
    remote_addr = models.GenericIPAddressField()
    path = models.CharField(max_length=128)
    cookies = models.CharField(max_length=256)
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)
