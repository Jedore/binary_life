# Create your models here.

from django.db import models
from django.utils import timezone


# Create your models here.


class ArticleType(models.Model):
    name = models.CharField(max_length=16)


class Article(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=1024, null=True, default=None)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)
    article_type = models.ForeignKey(ArticleType, related_name='articles', null=True, on_delete=models.SET_NULL)


class BinaryLifeViews(models.Model):
    username = models.CharField(max_length=32)
    is_anonymous = models.BooleanField()
    is_superuser = models.BooleanField()
    scheme = models.CharField(max_length=16)
    remote_addr = models.GenericIPAddressField()
    path = models.CharField(max_length=128)
    cookies = models.CharField(max_length=256)
    article = models.ForeignKey(Article, related_name='views', null=True, default=None,on_delete=models.SET_NULL)
