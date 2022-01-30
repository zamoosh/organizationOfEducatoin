from django.urls import path
from lesson.serializer import *

app_name = 'api'
urlpatterns = [
    path('lesson/', LessonList.as_view(), name='lessons'),
    path('lesson/<int:pk>', LessonDetail.as_view(), name='lesson')
]
