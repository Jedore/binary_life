from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from common.models import Article
from common.models import ArticleType
import json


# Create your views here.


def control(request):
    return render(request, 'control/base.html')


class PublishView(View):
    def get(self, request):
        article_types = ArticleType.objects.all()
        return render(request, 'control/publish.html', locals())

    def post(self, request):
        data = json.loads(request.body)
        title = data.get('title', '')
        content = data.get('content', '')
        article_type = data.get('article_type', '')

        Article.objects.create(title=title, content=content, article_type=ArticleType.objects.get(name=article_type))

        return JsonResponse({"ret": "SUCCESS"})


class ArticleTypeView(View):
    def get(self, request):
        article_types = ArticleType.objects.all()
        return render(request, 'control/article_type.html', locals())

    def post(self, request):
        article_type = json.loads(request.body).get('name', '')
        ArticleType.objects.create(name=article_type)
        return JsonResponse({"ret": "SUCCESS"})


class ArticleView(View):
    def get(self, request):
        articles = Article.objects.all().order_by('-create_time')
        return render(request, 'control/article.html', locals())

    def post(self, request):
        pass
