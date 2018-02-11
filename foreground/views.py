from django.shortcuts import render

from common.models import Article
from common.models import ArticleType


# Create your views here.


def index(request):
    articles = Article.objects.all().order_by("-create_time")
    article_types = ArticleType.objects.all().order_by("id")
    return render(request, 'foreground/index.html', locals())
