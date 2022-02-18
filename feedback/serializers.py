from rest_framework import serializers
from .models import *


class FeedbackSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        model = Feedback
        fields = ['title', 'description', 'author']
