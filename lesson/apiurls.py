from django.urls import path
from lesson.apiviews import *

app_name = 'lesson api'
urlpatterns = [
    path('lessons/', LessonListForUpdateTable.as_view(), name='lessons'),
    path('lesson/<int:pk>/edit/', LessonEditForUpdateTable.as_view(), name='lesson edit'),

]
