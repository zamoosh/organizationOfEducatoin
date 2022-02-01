from django.urls import path
from .views import login_page, test, test2

app_name = 'test'
urlpatterns = [
    path('', login_page, name='login'),
    path('api/', test, name='test'),
    path('test/', test2, name='test2')
]
