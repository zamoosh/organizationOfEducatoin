from .imports import *


class LessonListForUpdateTable(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializerForUpdateTable
