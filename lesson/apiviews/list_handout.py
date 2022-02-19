from .imports import *


class ListHandout(ListAPIView):
    queryset = Handout.objects.all()
    serializer_class = HandoutSerializer
