from django.urls import path, re_path

from .views import *

app_name = 'non_technical'
urlpatterns = [
    path("", index, name='index'),
    re_path(r"article/(?P<article_id>\d+)/(#.+)?", article, name='article'),
    path("type_articles/<int:type_id>", type_articles, name='type_articles'),
    path("tag_articles/<int:tag_id>", tag_articles, name='tag_articles'),
    path("commit_comment/", commit_comment, name='comment'),
]
