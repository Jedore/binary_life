from django.urls import path

from .views import *

urlpatterns = [
    path("articles/<int:article_id>", ArticleView.as_view()),
    path("type_articles/<int:type_id>", ArticleTypeView.as_view()),
]
