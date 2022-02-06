from .imports import *


class EditNotification(RetrieveUpdateDestroyAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer
