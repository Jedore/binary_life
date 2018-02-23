from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common.models import Article
from common.models import ArticleType
from common.utils import add_total_views


# Create your views here.


@add_total_views
@require_http_methods(["GET"])
def index(request):
    articles = Article.objects.all().order_by("-create_time")
    article_types = ArticleType.objects.all().order_by("id")
    return render(request, 'foreground/index.html', locals())


@add_total_views
@require_http_methods(["GET"])
def article(request, article_id):
    article_types = ArticleType.objects.all().order_by("id")
    _article = get_object_or_404(Article, id=article_id)
    _article.views = _article.views + 1
    _article.save()
    return render(request, "foreground/article.html", locals())


@add_total_views
@require_http_methods(["GET"])
def type_article(request, type_id):
    article_types = ArticleType.objects.all().order_by("id")
    articles = Article.objects.filter(article_type=type_id).order_by("-create_time")
    return render(request, "foreground/index.html", locals())
