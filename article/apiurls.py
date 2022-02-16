from django.urls import path
from article.apiviews import *

app_name = 'article'
urlpatterns = [
    path('articles/master/', list_article_master, name='list article master'),
    path('articles/student/', list_article_student, name='list article student'),
    path('article/<int:pk>/', EditArticle.as_view(), name='edit article'),
]
