from .imports import *


class EditLesson(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializerForUpdateTable
