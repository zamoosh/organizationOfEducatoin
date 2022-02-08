from django.urls import path
from .views import *

app_name = 'lesson and notification'
urlpatterns = [
    path('', show_lesson, name='list lesson'),
    path('save/', save_lesson, name='save lesson'),
    path('details/<int:pk>', detail_lesson, name='details lesson'),

    path('notification/', show_notification, name='show notification'),
    path('save/notification/', save_notification, name='save notification'),

    path('test-render/', test_render, name='render the test'),
    path('test/', test, name='test for csrf')
]
