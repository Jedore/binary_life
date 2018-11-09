from django.contrib.auth.views import login_required
from django.urls import path, register_converter

from . import converters
from .views import *

register_converter(converters.BoolConverter, 'bool')

app_name = 'background'
urlpatterns = [
    path('', login_required(BackgroundView.as_view()), name='background'),
    path('publish/', login_required(PublishView.as_view()), name='publish'),
    path('article_type/', login_required(ArticleTypeView.as_view()), name='article_type'),
    path('article/', login_required(ArticleView.as_view()), name='article'),
    path('article/hide_show/<int:article_id>/<bool:is_hide>/', login_required(article_hide_show), name='article_hs'),
    path('article/del/<int:article_id>/', login_required(article_del), name='article_del'),
]
