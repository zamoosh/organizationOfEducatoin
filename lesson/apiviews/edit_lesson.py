from .imports import *

ACCEPTED_EXTENSIONS = ['png', 'jpeg', 'jpg']


class EditLesson(RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        lesson = Lesson.objects.get(id=kwargs['pk'])
        context = {'request': request}
        return Response(LessonSerializerForUpdateTable(lesson, context=context).data, status=HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        if request.method == 'PUT':
            lesson = get_object_or_404(Lesson, id=kwargs['pk'])
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
            lesson.save()
            return Response(LessonSerializerForUpdateTable(lesson, context=context).data, status=HTTP_200_OK)
        return Response(None, status=HTTP_405_METHOD_NOT_ALLOWED)

    serializer_class = LessonSerializerForUpdateTable
    permission_classes = [IsAdminUser]
