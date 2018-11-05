from django.shortcuts import get_object_or_404
from django.shortcuts import render

from common.models import Article
from common.models import ArticleType
from common.views import BaseView


# Create your views here.


class IndexView(BaseView):
    def get(self, request):
        super(IndexView, self).get(request)
        articles = Article.objects.all().order_by("-create_time")
        article_types = ArticleType.objects.all().order_by("id")
        return render(request, 'foreground/index.html', locals())


class ArticleView(BaseView):
    def get(self, request, article_id):
        super(ArticleView, self).get(request)
        article_types = ArticleType.objects.all().order_by("id")
        article = get_object_or_404(Article, id=article_id)
        return render(request, "foreground/article.html", locals())


class ArticleTypeView(BaseView):
    def get(self, request, type_id):
        super(ArticleTypeView, self).get(request)
        article_types = ArticleType.objects.all().order_by("id")
        articles = Article.objects.filter(article_type=type_id).order_by("-create_time")
        return render(request, "foreground/index.html", locals())
