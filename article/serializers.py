from article.models import Article
from rest_framework.serializers import ModelSerializer


class ArticleSerializer(ModelSerializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        model = Article
        fields = '__all__'
