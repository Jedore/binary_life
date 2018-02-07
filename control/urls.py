from django.urls import path
from .views import *

urlpatterns = [
    path('', control),
    path('publish/', PublishView.as_view()),
    path('article_type/', ArticleTypeView.as_view()),
    path('article/', ArticleView.as_view()),
]
