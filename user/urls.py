from django.urls import path
from . import views as v
from django.views.generic import TemplateView


app_name = "user"
urlpatterns = [
     path('signin/', v.sign_in, name="signin"),
     path('signout/', v.sign_out, name="signout"),
     path('change_password/', v.change_password, name="change_password"),
     path('test/', TemplateView.as_view(template_name='index.html'), name='test')

]
