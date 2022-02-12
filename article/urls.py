from django.urls import path
from .views import *

app_name = 'article'
urlpatterns = [
    path('', show_article, name='show article'),
    # path('details/<int:pk>', '', name='details'),
]
