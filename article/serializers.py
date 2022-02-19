from article.models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['name', 'title', 'subject', 'author', 'description', 'is_confirmed', 'is_master', 'file']
