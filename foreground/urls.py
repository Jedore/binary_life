from django.urls import path

from .views import *

app_name = 'foreground'
urlpatterns = [
    path("article/<int:article_id>", article, name='article'),
    path("type_articles/<int:type_id>", type_articles, name='type_articles'),
    path("tag_articles/<int:tag_id>", tag_articles, name='tag_articles'),
    path("commit_comment/", commit_comment, name='comment'),
]
