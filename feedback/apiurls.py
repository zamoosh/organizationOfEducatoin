from django.urls import path
from feedback.apiviews import *

app_name = 'feedback api'
urlpatterns = [
    path('feedbacks/', ListFeedback.as_view(), name='feedbacks'),
    path('feedback/<int:pk>/', EditFeedback.as_view(), name='feedback edit'),
]
