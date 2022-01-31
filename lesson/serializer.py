from lesson.models import *
from rest_framework.serializers import ModelSerializer


class LessonSerializer(ModelSerializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        model = Lesson
        fields = ['name', 'title', 'university_name', 'student', 'student_list', 'grades_list', 'create', 'update']


class LessonSerializerForUpdateTable(ModelSerializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        model = Lesson
        fields = ['name', 'title', 'university_name']
