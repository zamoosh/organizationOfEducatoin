from django.urls import path
from . import views as v
from django.views.generic import TemplateView


app_name = "user"
urlpatterns = [
     path('login/', v.sign_in, name="login"),
     path('logout/', v.sign_out, name="logout"),
     path('test/', TemplateView.as_view(template_name='index.html'), name='test')

]
