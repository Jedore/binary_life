import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from common.models import Article
from common.models import ArticleType
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


class BackgroundView(View):
    def get(self, request):
        return render(request, 'background/base.html')


class PublishView(View):
    def get(self, request):
        article_types = ArticleType.objects.all()
        return render(request, 'background/publish.html', locals())

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
        return render(request, 'background/article_type.html', locals())

    def post(self, request):
        article_type = json.loads(request.body).get('name', '')
        ArticleType.objects.create(name=article_type)
        return JsonResponse({"ret": "SUCCESS"})

    def delete(self, request):
        data = json.loads(request.body)
        type_id = data.get("typeId", 0)
        try:
            article_type = ArticleType.objects.get(id=type_id)
            article_type.delete()
            return JsonResponse({"ret_code": 0})
        except ObjectDoesNotExist:
            return JsonResponse({"ret_code": 1, "error": "ObjectDoesNotExist"})


class ArticleView(View):
    def get(self, request):
        articles = Article.objects.all().order_by('-create_time')
        return render(request, 'background/article.html', locals())

    def delete(self, request):
        data = json.loads(request.body)
        article_id = data.get("articleId", 0)
        try:
            article = Article.objects.get(id=article_id)
            article.delete()
            return JsonResponse({"ret_code": 0})
        except ObjectDoesNotExist as e:
            return JsonResponse({"ret_code": 1, "error": "ObjectDoesNotExist"})
