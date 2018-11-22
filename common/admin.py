from django.contrib import admin
from .models import *


# Register your models here.

class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time', 'update_time', ]


class ArticleTagsAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time', 'update_time', ]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'summary', 'content', 'create_time', 'update_time',
                    'is_hide', 'page_view', 'unique_view', 'ip_view', ]


class ViewsRecordAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_anonymous', 'is_superuser', 'scheme', 'remote_addr', 'path', 'cookies',
                    'create_time', 'update_time', ]


class ArticleCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'create_time', 'article', 'reply', ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
admin.site.register(ArticleTags, ArticleTagsAdmin)
admin.site.register(ArticleComments, ArticleCommentsAdmin)
admin.site.register(ViewsRecord, ViewsRecordAdmin)
