from rest_framework import serializers


class ArticleCreateDto(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    title = serializers.CharField()
    description = serializers.CharField()
    # name = serializers.CharField(max_length=50, blank=False, default='article')
    # subject = serializers.CharField(max_length=255, blank=False)
    # author = serializers.CharField(max_length=255, blank=True, default='admin')
    # is_confirmed = serializers.BooleanField(default=False)
    # is_master = serializers.BooleanField(default=False)
    # file = serializers.FileField()
