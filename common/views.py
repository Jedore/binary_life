import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import redirect, reverse
from foreground.views import index


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
    return redirect(reverse(index))
