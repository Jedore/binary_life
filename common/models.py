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
    views = models.IntegerField(default=0)
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)
    article_type = models.ForeignKey(ArticleType, related_name='articles', null=True, on_delete=models.SET_NULL)


class BinaryLife(models.Model):
    views = models.IntegerField(default=0)
