from article.models import Article
from rest_framework.serializers import ModelSerializer


class ArticleSerializer(ModelSerializer):
    def update(self, instance, validated_data):
        instance.name = validated_data['name']
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
        exclude = ['create', 'update']
