from .imports import *


class ListLesson(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializerForUpdateTable
