from django.contrib import admin
from article.models import *


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('title', {'fields': ['title']}),
        ('subject of this article', {'fields': ['subject']}),
        ('author of this article', {'fields': ['author']}),
        ('description', {'fields': ['description']}),
        ('file', {'fields': ['file']}),
        ('is confirmed by the master?', {'fields': ['is_confirmed']}),
        ('is written by master?', {'fields': ['is_master']}),

    ]
    list_display = ['name', 'title', 'subject', 'author', 'create', 'update', 'is_master', 'is_confirmed', 'id']
    list_editable = ['author', 'is_confirmed']
    ordering = ['is_confirmed', 'author', 'create']


admin.site.register(Article, ArticleAdmin)
