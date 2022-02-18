from django.contrib import admin
from .models import *


class FeedbackAdmin(admin.ModelAdmin):
    fieldsets = [
        ('title', {'fields': ['title']}),
        ('author', {'fields': ['author']}),
        ('description', {'fields': ['description']}),
    ]
    list_display = ['title', 'author', 'description', 'create', 'update']


admin.site.register(Feedback, FeedbackAdmin)
