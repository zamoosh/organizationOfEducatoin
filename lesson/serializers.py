from lesson.models import *
from rest_framework import serializers


class LessonSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        model = Lesson
        fields = ['name',
                  'title',
                  'university_name',
                  'student', 'student_list',
                  'grades_list',
                  'create',
                  'update'
                  ]


class LessonSerializerForUpdateTable(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        model = Lesson
        fields = ['name', 'title', 'university_name', 'image']


class HandoutSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Handout
        fields = ['lesson', 'title', 'author']


class NotificationSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        model = Notifications
        fields = ['title', 'description', 'slug', 'author']
