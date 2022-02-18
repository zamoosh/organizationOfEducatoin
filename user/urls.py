from django.urls import path
from .views import *

app_name = "user"
urlpatterns = [
    # path('', login, name="login"),
    path('requests/',  requests),
]
