from .imports import *


class ListNotification(ListAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer
