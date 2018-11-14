from django.contrib.auth.views import login_required
from django.urls import path, register_converter

from . import converters
from .views import *

register_converter(converters.BoolConverter, 'bool')

app_name = 'background'
urlpatterns = [
    path('', login_required(index), name='background'),
    path('publish/', login_required(publish), name='publish'),
    path('article_type/', login_required(article_types), name='article_type'),
    path('article_type/del/', login_required(article_type_del), name='article_type_del'),
    path('article_type/add/', login_required(article_type_add), name='article_type_add'),
    path('article/', login_required(articles), name='article'),
    path('article_add/', login_required(article_add), name='article_add'),
    path('article/hide_show/<int:article_id>/<bool:is_hide>/', login_required(article_hide_show), name='article_hs'),
    path('article/del/<int:article_id>/', login_required(article_del), name='article_del'),
]
