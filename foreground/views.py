from django.shortcuts import render

from common.models import Article


# Create your views here.


def index(request):
    articles = Article.objects.all().order_by("-create_time")
    return render(request, 'foreground/index.html', locals())
