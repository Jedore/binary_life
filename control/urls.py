from django.urls import path
from .views import *

urlpatterns = [
    path('', control),
    path('publish', publish),
]
