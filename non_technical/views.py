from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from common.models import Article
from common.models import ArticleComments
from common.models import ArticleTags
from common.views import article_page_view
from common.views import process_str
from common.views import record_page_view


# Create your views here.


@record_page_view
def index(request):
    articles = Article.objects.filter(is_hide=False, non_technical=True).order_by("-create_time")
    # types = ArticleType.objects.filter(non_technical=True)
    tags = ArticleTags.objects.filter(non_technical=True)
    # comments = ArticleComments.objects.all()[:5]
    return render(request, 'non_technical/index.html', locals())


@record_page_view
@article_page_view
def article(request, article_id):
    # types = ArticleType.objects.all()
    tags = ArticleTags.objects.filter(non_technical=True)
    # comments = ArticleComments.objects.all()[:5]
    article = get_object_or_404(Article, id=article_id)
    return render(request, "non_technical/article.html", locals())


@record_page_view
def type_articles(request, type_id):
    # types = ArticleType.objects.all()
    tags = ArticleTags.objects.filter(non_technical=True)
    # comments = ArticleComments.objects.all()[:5]
    articles = Article.objects.filter(article_type=type_id, is_hide=False, non_technical=True).order_by("-create_time")
    return render(request, "non_technical/index.html", locals())


@record_page_view
def tag_articles(request, tag_id):
    # types = ArticleType.objects.all()
    tags = ArticleTags.objects.filter(non_technical=True)
    # comments = ArticleComments.objects.all()[:5]
    articles = Article.objects.filter(tags=tag_id, is_hide=False, non_technical=True).order_by("-create_time")
    return render(request, "non_technical/index.html", locals())


@record_page_view
def commit_comment(request):
    if request.method != "POST":
        return
    name = process_str(request.POST.get("name"))
    comment = process_str(request.POST.get("comment"))
    article_id = process_str(request.POST.get("article_id"))
    reply_id = process_str(request.POST.get("reply_id"))
    
    ret = {}
    try:
        if not name or not comment or not article_id:
            raise Exception("parameters error")
        article = Article.objects.filter(id=int(article_id)).first()
        if reply_id:
            reply = ArticleComments.objects.filter(id=int(reply_id)).first()
        else:
            reply = None
        if not article:
            raise Exception("article not exist")
        is_author = True if request.user.username == article.author else False
        comment = ArticleComments.objects.create(name=name, is_author=is_author, comment=comment, article=article,
                                                 reply=reply)
        ret["create_time"] = comment.create_time.strftime("%Y-%m-%d %H:%M")
        ret["id"] = comment.id
        ret["is_author"] = is_author
        if reply_id:
            ret["reply_id"] = reply_id
    except Exception as e:
        ret["failed"] = str(e)
    return JsonResponse(ret)
