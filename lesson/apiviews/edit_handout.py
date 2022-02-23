from .imports import *


class EditHandout(RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        handout = get_object_or_404(Handout, id=kwargs['pk'])
        context = {'request': request}
        return Response(HandoutSerializer2(handout, context=context).data, status=HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        if request.method == 'PUT' or request.method == 'PATCH':
            handout = Handout.objects.get(id=kwargs['pk'])
            handout.lesson = Lesson.objects.get(id=request.data.get('lesson'))
            handout.title = request.data.get('title')
            handout.author = request.data.get('author')
            if request.FILES:
                handout.file.delete(save=False)
                handout.file = request.FILES.get('file')
            context = {'request': request}
            handout.save()
            return Response(HandoutSerializer2(handout, context=context).data, status=HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)

    serializer_class = HandoutSerializer
    permission_classes = [IsAdminUser]
