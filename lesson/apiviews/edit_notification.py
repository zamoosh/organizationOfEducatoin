from .imports import *


class EditNotification(RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        notification = get_object_or_404(Lesson, id=kwargs['pk'])
        context = {'request': request}
        return Response(NotificationSerializer(notification, context=context).data, status=HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        if request.method == 'PATCH' or request.method == 'PATCH':
            notification = Notifications.objects.get(id=kwargs['pk'])
            notification.title = request.data.get('title')
            notification.description = request.data.get('description')
            notification.author = request.data.get('author')
            context = {'request': request}
            notification.save()
            return Response(NotificationSerializer(notification, context=context).data, status=HTTP_200_OK)
        return Response(None, status=HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)

    serializer_class = NotificationSerializer
    permission_classes = [IsAdminUser]
