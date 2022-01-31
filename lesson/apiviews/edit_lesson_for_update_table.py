from .imports import *


class LessonEditForUpdateTable(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializerForUpdateTable
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'
