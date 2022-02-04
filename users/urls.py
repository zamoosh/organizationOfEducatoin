from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', profile),
    path('lessson/', lessons),
    path('notes/', notes),
    path('article/', article),
    path('', index),
    path('notifications/', notifications)
]
