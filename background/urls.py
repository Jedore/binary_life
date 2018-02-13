from django.contrib.auth.views import login_required
from django.urls import path

from .views import *

urlpatterns = [
    path('', login_required(BackgroundView.as_view())),
    path('publish/', login_required(PublishView.as_view())),
    path('article_type/', login_required(ArticleTypeView.as_view())),
    path('article/', login_required(ArticleView.as_view())),
]
