from django.urls import path
from lesson.apiviews import *

app_name = 'lesson api'
urlpatterns = [
    path('lessons/', ListLesson.as_view(), name='lessons'),
    path('lesson/<int:pk>/', EditLesson.as_view(), name='lesson edit'),
    path('notifications/', ListNotification.as_view(), name='notifications'),
    path('notification/<int:pk>/', EditNotification.as_view(), name='notification edit')

]
