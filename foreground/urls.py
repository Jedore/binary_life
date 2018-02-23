from django.urls import path
from .views import *

urlpatterns = [
    path("articles/<int:article_id>", article),
    path("type_articles/<int:type_id>", type_article),
]
