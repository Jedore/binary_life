from django.urls import path
from .views import *

urlpatterns = [
    path('', BackgroundView.as_view()),
    path('publish/', PublishView.as_view()),
    path('article_type/', ArticleTypeView.as_view()),
    path('article/', ArticleView.as_view()),
]
