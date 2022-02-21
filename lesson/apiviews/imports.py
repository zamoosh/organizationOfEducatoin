from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import *
from lesson.models import *
from lesson.serializers import *
