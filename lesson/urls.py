from django.urls import path
from .views import *

app_name = 'lesson'
urlpatterns = [
    path('add/lesson/', add_lesson, name='add lesson'),
    path('save/lesson/', save_lesson, name='save lesson'),
    path('add/notification/', add_notification, name='add notification'),
    path('save/notification/', save_notification, name='save notification')
]
