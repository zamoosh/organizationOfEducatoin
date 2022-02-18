from article.models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField(method_name='get_file_url')

    def get_file_url(self, obj):
        return self.context['server'] + obj.file.url

    class Meta:
        model = Article
        fields = ['name', 'title', 'subject', 'author', 'description', 'is_confirmed', 'is_master', 'file']
