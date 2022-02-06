from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from lesson.models import *
from lesson.serializers import LessonSerializerForUpdateTable, NotificationSerializer
