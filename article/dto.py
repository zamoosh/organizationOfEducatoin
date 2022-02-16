from rest_framework import serializers


class ArticleCreateDto(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    title = serializers.CharField()
    description = serializers.CharField()
