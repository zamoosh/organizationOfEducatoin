from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from lesson.models import *
from lesson.serializer import LessonSerializerForUpdateTable
