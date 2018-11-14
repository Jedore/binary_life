import sys

from django.contrib import messages
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from common.models import Article
from common.models import ArticleTags
from common.models import ArticleType
from common.models import ViewsRecord
from common.views import process_str
from common.views import record_page_view


# Create your views here.


@record_page_view
def index(request):
    articles = Article.objects.all()
    all_views = ViewsRecord.objects.all().count()
    visitors = ViewsRecord.objects.filter(is_superuser=False).count()
    return render(request, 'background/dashboard.html', locals())


@record_page_view
def publish(request):
    article_id = request.GET.get('article_id')
    if article_id is not None:
        article = get_object_or_404(Article, id=article_id)
    article_types = ArticleType.objects.all()
    return render(request, 'background/publish.html', locals())


@record_page_view
def article_add(request):
    title = process_str(request.POST.get('title'))
    content = request.POST.get('content')
    article_type = process_str(request.POST.get('article_type'))
    tags = process_str(request.POST.get('tags'))
    is_hide = process_str(request.POST.get('is_hide'))
    article_id = request.POST.get('article_id')
    try:
        if not title or not tags or not article_type or not content or not is_hide:
            raise Exception("parameter error")
        if is_hide == 'True':
            is_hide = True
        elif is_hide == 'False':
            is_hide = False
        else:
            raise Exception('is_hide error')
        tags = tags.split()
        with transaction.atomic():
            for tag in tags:
                ArticleTags.objects.get_or_create(name=tag)
            if request.POST.get('method') == 'post':
                article = Article.objects.create(title=title, content=content, is_hide=is_hide,
                                                 article_type=ArticleType.objects.get(id=article_type))
                article.tags.set(list(ArticleTags.objects.filter(name__in=tags)))
            elif request.POST.get('method') == 'put':
                article = Article.objects.filter(id=article_id).first()
                if not article:
                    raise Exception('article not exist')
                article.title = title
                article.content = content
                article.article_type = get_object_or_404(ArticleType, id=article_type)
                article.is_hide = is_hide
                article.save()
                article.tags.set(list(ArticleTags.objects.filter(name__in=tags)), clear=True)
        messages.success(request, "success")
    except Exception as e:
        messages.error(request, "failed: {}".format(sys.exc_info()[1]))
    article_types = ArticleType.objects.all()
    return render(request, 'background/publish.html', locals())


@record_page_view
def article_types(request):
    article_types = ArticleType.objects.all()
    return render(request, 'background/article_type.html', locals())


@record_page_view
def articles(request):
    articles = Article.objects.all().order_by('-create_time')
    return render(request, 'background/article.html', locals())


@record_page_view
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


@record_page_view
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


@record_page_view
def article_type_del(request):
    if request.method != 'POST':
        return
    type_id = process_str(request.POST.get('type_id'))
    ret = {}
    try:
        article_type = ArticleType.objects.filter(id=type_id).first()
        if not article_type:
            raise Exception('article type not exist')
        article_type.delete()
    except Exception as e:
        ret['failed'] = str(e)
    return JsonResponse(ret)


@record_page_view
def article_type_add(request):
    if request.method != 'POST':
        return
    type_name = process_str(request.POST.get('type_name'))
    ret = {}
    try:
        if not type_name:
            raise Exception("name is null")
        article_type = ArticleType.objects.create(name=type_name)
        ret["id"] = article_type.id
    except Exception as e:
        ret["failed"] = str(e)
    return JsonResponse(ret)
