from django.shortcuts import get_object_or_404
from django.shortcuts import render

from common.models import Article
from common.models import ArticleTags
from common.models import ArticleType
from common.views import record_view


# Create your views here.


@record_view
def index(request):
    articles = Article.objects.filter(is_hide=False).order_by("-create_time")
    types = ArticleType.objects.all()
    tags = ArticleTags.objects.all()
    return render(request, 'foreground/index.html', locals())


@record_view
def article(request, article_id):
    types = ArticleType.objects.all()
    tags = ArticleTags.objects.all()
    article = get_object_or_404(Article, id=article_id)
    return render(request, "foreground/article.html", locals())


@record_view
def type_articles(request, type_id):
    types = ArticleType.objects.all()
    tags = ArticleTags.objects.all()
    articles = Article.objects.filter(article_type=type_id, is_hide=False).order_by("-create_time")
    return render(request, "foreground/index.html", locals())


@record_view
def tag_articles(request, tag_id):
    types = ArticleType.objects.all()
    tags = ArticleTags.objects.all()
    articles = Article.objects.filter(tags=tag_id, is_hide=False).order_by("-create_time")
    return render(request, "foreground/index.html", locals())
