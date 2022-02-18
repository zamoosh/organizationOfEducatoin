from .imports import *


class ListFeedback(ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
