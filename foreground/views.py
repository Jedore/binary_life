from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404

from common.models import Article
from common.models import ArticleType


# Create your views here.


@require_http_methods(["GET"])
def index(request):
    articles = Article.objects.all().order_by("-create_time")
    article_types = ArticleType.objects.all().order_by("id")
    return render(request, 'foreground/index.html', locals())


@require_http_methods(["GET"])
def article(request, article_id):
    article_types = ArticleType.objects.all().order_by("id")
    _article = get_object_or_404(Article, id=article_id)
    return render(request, "foreground/article.html", locals())


@require_http_methods(["GET"])
def type_article(request, type_id):
    article_types = ArticleType.objects.all().order_by("id")
    articles = Article.objects.filter(article_type=type_id)
    return render(request, "foreground/index.html", locals())
