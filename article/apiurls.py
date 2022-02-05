from django.urls import path
from article.apiviews import *

app_name = 'article'
urlpatterns = [
    path('articles/', ListArticle.as_view(), name='list article'),
    path('article/<int:pk>', EditArticle.as_view(), name='edit article'),
]
