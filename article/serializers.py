from article.models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField(method_name='get_file_url')

    def get_file_url(self, obj):
        return self.context['server'] + obj.file.url

    def update(self, instance, validated_data):
        instance.article = validated_data['name']
        instance.title = validated_data['title']
        instance.subject = validated_data['subject']
        instance.author = validated_data['author']
        instance.description = validated_data['description']
        instance.is_confirmed = validated_data['is_confirmed']
        if 'file' in validated_data:
            instance.file = validated_data['file']
        instance.save()
        return instance

    def create(self, validated_data):
        pass

    class Meta:
        model = Article
        fields = ['name', 'title', 'subject', 'author', 'description', 'is_confirmed', 'is_master', 'file']
