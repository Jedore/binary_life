import sys

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from common.models import Article
from common.models import ArticleType
from common.models import ViewsRecord
from common.views import BaseView


# Create your views here.


class BackgroundView(BaseView):
    def get(self, request):
        super(BackgroundView, self).get(request)
        articles = Article.objects.all()
        all_views = ViewsRecord.objects.all().count()
        visitors = ViewsRecord.objects.filter(is_superuser=False).count()
        return render(request, 'background/dashboard.html', locals())


class PublishView(BaseView):
    def get(self, request):
        super(PublishView, self).get(request)
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


class ArticleTypeView(BaseView):
    def get(self, request):
        super(ArticleTypeView, self).get(request)
        article_types = ArticleType.objects.all().order_by('-create_time')
        return render(request, 'background/article_type.html', locals())


class ArticleView(BaseView):
    def get(self, request):
        super(ArticleView, self).get(request)
        articles = Article.objects.all().order_by('-create_time')
        return render(request, 'background/article.html', locals())


def article_hide_show(request, article_id, is_hide):
    ret = {}
    try:
        article = Article.objects.filter(id=article_id).first()
        if not article:
            raise Exception('article not exist')
        if is_hide != article.is_hide:
            raise Exception('is_hide status not match, please refresh')
        if article.is_hide:
            article.is_hide = False
        else:
            article.is_hide = True
        article.save()
        ret['is_hide'] = str(article.is_hide)
    except Exception as e:
        ret['failed'] = str(e)
    return JsonResponse(ret)


def article_del(request, article_id):
    ret = {}
    try:
        article = Article.objects.filter(id=article_id).first()
        if not article:
            raise Exception('article not exist')
        article.delete()
    except Exception as e:
        ret['failed'] = str(e)
    return JsonResponse(ret)


def article_type_del(request, article_type_id):
    ret = {}
    try:
        article_type = ArticleType.objects.filter(id=article_type_id).first()
        if not article_type:
            raise Exception('article type not exist')
        article_type.delete()
    except Exception as e:
        ret['failed'] = str(e)
    return JsonResponse(ret)
