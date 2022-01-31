from django.urls import path
from lesson.apiviews import *

app_name = 'api'
urlpatterns = [
    path('lessons/', LessonListForUpdateTable.as_view(), name='lessons'),
    path('lesson/<int:pk>', LessonEditForUpdateTable.as_view(), name='lesson')
]
