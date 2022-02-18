from .imports import *

ACCEPTED_EXTENSIONS = ['png', 'jpeg', 'jpg']


class EditLesson(RetrieveUpdateDestroyAPIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def put(self, request, *args, **kwargs):
        if request.method == 'PUT':
            lesson = Lesson.objects.get(id=kwargs['pk'])
            lesson.name = request.POST.get('name')
            lesson.title = request.POST.get('title')
            lesson.university_name = request.POST.get('university_name')
            if request.FILES:
                extension = request.FILES.get('image').name
                extension = extension.split('.')[-1]
                if extension in ACCEPTED_EXTENSIONS:
                    lesson.image.delete(save=False)
                    lesson.image = request.FILES.get('image')
                else:
                    return Response(data='only images can be pass', status=HTTP_400_BAD_REQUEST, exception=True)
            context = {'request': request}
            serializer = LessonSerializerForUpdateTable(lesson, context=context)
            lesson.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(None, status=HTTP_405_METHOD_NOT_ALLOWED)

    def get(self, request, *args, **kwargs):
        lesson = Lesson.objects.get(id=kwargs['pk'])
        context = {'request': request}
        serializer = LessonSerializerForUpdateTable(lesson, context=context)
        return Response(serializer.data, status=HTTP_200_OK)

    def get_serializer_class(self):
        return LessonSerializerForUpdateTable

    permission_classes = [IsAdminUser]
