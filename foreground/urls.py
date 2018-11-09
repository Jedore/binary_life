from django.urls import path

from .views import *

app_name = 'foreground'
urlpatterns = [
    path("articles/<int:article_id>", ArticleView.as_view(), name='article'),
    path("type_articles/<int:type_id>", ArticleTypeView.as_view(), name='article_type'),
]
