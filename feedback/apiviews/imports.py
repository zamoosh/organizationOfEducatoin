from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from feedback.models import *
from feedback.serializers import FeedbackSerializer
