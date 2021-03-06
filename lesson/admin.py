from django.contrib import admin
from .models import *


class LessonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('title', {'fields': ['title']}),
        ('university name', {'fields': ['university_name']}),
        ('image', {'fields': ['image']}),
        ('student', {'fields': ['student']}),
    ]
    list_display = ['name', 'title', 'university_name', 'create', 'update', 'id']


class HandoutAdmin(admin.ModelAdmin):
    fieldsets = [
        ('lesson name', {'fields': ['lesson']}),
        ('title', {'fields': ['title']}),
        ('description', {'fields': ['description']}),
        ('file', {'fields': ['file']}),
        ('author', {'fields': ['author']}),
    ]
    list_display = ['lesson', 'title', 'create', 'update']


class NotificationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    fieldsets = [
        ('title', {'fields': ['title']}),
        ('slug', {'fields': ['slug']}),
        ('author', {'fields': ['author']}),
        ('description', {'fields': ['description']}),
    ]
    list_display = ['title', 'author', 'description', 'create', 'update', 'id']


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Handout, HandoutAdmin)
admin.site.register(Notifications, NotificationAdmin)
