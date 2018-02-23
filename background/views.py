import sys

from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View

from common.models import Article
from common.models import ArticleType


# Create your views here.


class BackgroundView(View):
    def get(self, request):
        return render(request, 'background/base.html')


class PublishView(View):
    def get(self, request):
        article_id = request.GET.get('articleId')
        if article_id is not None:
            article = get_object_or_404(Article, id=article_id)
        article_types = ArticleType.objects.all()
        return render(request, 'background/publish.html', locals())

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        article_type = request.POST.get('article_type')

        try:
            if request.POST.get('method') == 'post':
                Article.objects.create(title=title, content=content,
                                       article_type=ArticleType.objects.get(id=article_type))
            elif request.POST.get('method') == 'put':
                article_id = request.POST.get('articleId')
                article = get_object_or_404(Article, id=article_id)
                article.title = title
                article.content = content
                article.article_type = get_object_or_404(ArticleType, id=article_type)
                article.save()
            messages.success(request, "success")
        except:
            messages.error(request, "failed: {}".format(sys.exc_info()[1]))

        article_types = ArticleType.objects.all()

        return render(request, 'background/publish.html', locals())


class ArticleTypeView(View):
    def get(self, request):
        article_types = ArticleType.objects.all()
        return render(request, 'background/article_type.html', locals())

    def post(self, request):
        if request.POST.get('method') == 'post':
            article_type = request.POST.get('name')
            try:
                ArticleType.objects.create(name=article_type)
                messages.success(request, "success")
            except:
                messages.error(request, "failed: {}".format(sys.exc_info()[1]))
        elif request.POST.get('method') == 'delete':
            type_id = request.POST.get("typeId", 0)
            try:
                article_type = ArticleType.objects.get(id=type_id)
                article_type.delete()
                messages.success(request, "success")
            except:
                messages.error(request, "failed: {}".format(sys.exc_info()[1]))
        article_types = ArticleType.objects.all()
        return render(request, 'background/article_type.html', locals())


class ArticleView(View):
    def get(self, request):
        articles = Article.objects.all().order_by('-create_time')
        return render(request, 'background/article.html', locals())

    def post(self, request):
        if request.POST.get('method') == 'delete':
            article_id = request.POST.get("articleId", 0)
            try:
                article = Article.objects.get(id=article_id)
                article.delete()
                messages.success(request, "success")
            except:
                messages.error(request, "failed: {}".format(sys.exc_info()[1]))
        articles = Article.objects.all().order_by('-create_time')
        return render(request, 'background/article.html', locals())
