from lesson.models import *
from rest_framework import serializers


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'title', 'university_name', 'student', 'student_list', 'grades_list', 'create', 'update']


class LessonSerializerForUpdateTable(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'title', 'university_name', 'create', 'update', 'image', 'id']


class HandoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handout
        fields = ['lesson', 'title', 'author', 'file']


class HandoutSerializer2(serializers.ModelSerializer):
    lesson = serializers.SerializerMethodField()

    @staticmethod
    def get_lesson(obj):
        return {'id': obj.lesson.id, 'name': obj.lesson.name}

    class Meta:
        model = Handout
        fields = ['lesson', 'title', 'author', 'file']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['title', 'description', 'author']
