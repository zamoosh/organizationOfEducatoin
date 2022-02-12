from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from article.models import Article
from article.serializers import ArticleSerializer
