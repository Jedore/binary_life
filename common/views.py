import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import redirect, render_to_response

from .models import Article
from .models import ViewsRecord


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


def process_str(src):
    """ Process parameter for request form data
    """
    return src if src is None else src.strip()


def record_page_view(func):
    """ Decorator for recording views
    """
    
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_superuser:
            ViewsRecord.objects.create(
                username=request.user.username,
                is_anonymous=request.user.is_anonymous,
                is_superuser=request.user.is_superuser,
                scheme=request.scheme,
                remote_addr=request.environ['REMOTE_ADDR'],
                path=request.path,
                cookies=json.dumps(request.COOKIES),
            )
        return func(request, *args, **kwargs)
    
    return wrapper_func


def article_page_view(func):
    """page view for article"""
    
    def wrapper_func(request, article_id):
        if not request.user.is_superuser:
            article = Article.objects.filter(id=article_id).first()
            if article_id:
                article.page_view += 1
                article.save()
        return func(request, article_id)
    
    return wrapper_func


def custom_404_handler(request, exception, template_name="404.html"):
    response = render_to_response("common/404.html")
    response.status_code = 404
    return response
