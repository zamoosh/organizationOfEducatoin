from django.contrib import admin
from article.models import *


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('title', {'fields': ['title']}),
        ('subject of this article', {'fields': ['subject']}),
        ('author of this article', {'fields': ['author']}),
        ('description', {'fields': ['description']}),
        ('is confirmed by the master?', {'fields': ['is_confirmed']}),

    ]
    list_display = ['title', 'subject', 'author', 'create', 'update', 'is_confirmed']
    list_editable = ['author', 'is_confirmed']
    ordering = ['is_confirmed', 'author', 'create']


admin.site.register(Article, ArticleAdmin)
