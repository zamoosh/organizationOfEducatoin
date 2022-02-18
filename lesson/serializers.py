from lesson.models import *
from rest_framework import serializers
from jalali_date import datetime2jalali


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'title', 'university_name', 'student', 'student_list', 'grades_list', 'create', 'update']


class LessonSerializerForUpdateTable(serializers.ModelSerializer):
    # create = serializers.SerializerMethodField()
    #
    # def get_create(self, obj):
    #     return str(datetime2jalali(obj.create))

    class Meta:
        model = Lesson
        fields = ['name', 'title', 'university_name', 'create', 'update', 'image', 'id']


class HandoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handout
        fields = ['lesson', 'title', 'author']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['title', 'description', 'slug', 'author']
