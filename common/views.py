import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views import View

from .models import Article
from .models import BinaryLifeViews


# Create your views here.


def bl_login(requset):
    if requset.method == "POST":
        data = json.loads(requset.body)
        username = data.get('username', '')
        password = data.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(requset, user)
            return JsonResponse({"ret_code": 0})
        else:
            return JsonResponse({"ret_code": 1, "error": "user and password does't match."})


def bl_logout(request):
    logout(request)
    return redirect('/')


class BaseView(View):
    """
    Base View for foreground
    """

    def get(self, request):
        if request.path.startswith('/foreground/articles/'):
            article_id = request.path.split('/')[-1]
            article = get_object_or_404(Article, id=article_id)
        else:
            article = None
        BinaryLifeViews.objects.create(
            username=request.user.username,
            is_anonymous=request.user.is_anonymous,
            is_superuser=request.user.is_superuser,
            scheme=request.scheme,
            remote_addr=request.environ['REMOTE_ADDR'],
            path=request.path,
            cookies=json.dumps(request.COOKIES),
            article=article
        )
