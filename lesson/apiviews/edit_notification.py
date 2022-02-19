from .imports import *


class EditNotification(RetrieveUpdateDestroyAPIView):

    def get(self, request, *args, **kwargs):
        lesson = Notifications.objects.get(id=kwargs['pk'])
        context = {'request': request}
        serializer = NotificationSerializer(lesson, context=context)
        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        if request.method == 'PUT':
            notification = Notifications.objects.get(id=kwargs['pk'])
            notification.title = request.data.get('title')
            notification.description = request.data.get('description')
            notification.author = request.data.get('author')
            context = {'request': request}
            serializer = NotificationSerializer(notification, context=context)
            notification.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(None, status=HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        if request.method == 'PATCH':
            notification = Notifications.objects.get(id=kwargs['pk'])
            notification.title = request.data.get('title')
            notification.description = request.data.get('description')
            notification.author = request.data.get('author')
            context = {'request': request}
            serializer = NotificationSerializer(notification, context=context)
            notification.save()
            return Response(serializer.data, status=HTTP_200_OK)

    serializer_class = NotificationSerializer
    permission_classes = [IsAdminUser]
