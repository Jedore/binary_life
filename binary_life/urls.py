"""binary_life URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views import static

from common.views import bl_logout
from foreground.views import index

urlpatterns = [
    path('binary/', admin.site.urls),
    # path('login/', bl_login, name='login'),
    path('logout/', bl_logout, name='logout'),
    path('', index, name='index'),
    path('foreground/', include('foreground.urls')),
    path('background/', include('background.urls')),
    path('non_technical/', include('non_technical.urls')),
]

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}),
    ]

handler404 = 'common.views.custom_404_handler'
