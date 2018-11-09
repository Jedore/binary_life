from django.contrib.auth.views import login_required
from django.urls import path, register_converter

from . import converters
from .views import *

register_converter(converters.BoolConverter, 'bool')

urlpatterns = [
    path('', login_required(BackgroundView.as_view())),
    path('publish/', login_required(PublishView.as_view())),
    path('article_type/', login_required(ArticleTypeView.as_view())),
    path('article/', login_required(ArticleView.as_view())),
    path('article/hide_show/<int:article_id>/<bool:is_hide>/', login_required(article_hide_show)),
    path('article/del/<int:article_id>/', login_required(article_del)),
]
