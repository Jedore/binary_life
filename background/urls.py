from django.contrib.auth.views import login_required
from django.urls import path, register_converter

from . import converters
from .views import *

register_converter(converters.BoolConverter, 'bool')

app_name = 'background'
urlpatterns = [
    path('', login_required(index), name='background'),
    path('publish/', login_required(publish_get), name='publish_get'),
    path('publish_post/', login_required(publish_post), name='publish_post'),
    path('article_type/', login_required(article_types), name='article_type'),
    path('article_type/del/<int:article_type_id>/', login_required(article_type_del), name='article_type_del'),
    path('article/', login_required(articles), name='article'),
    path('article/hide_show/<int:article_id>/<bool:is_hide>/', login_required(article_hide_show), name='article_hs'),
    path('article/del/<int:article_id>/', login_required(article_del), name='article_del'),
]
