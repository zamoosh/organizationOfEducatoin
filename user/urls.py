from django.urls import path
from . import views as v


app_name = "user"
urlpatterns = [
     path('signin/', v.sign_in, name="signin"),
     path('signout/', v.sign_out, name="signout"),
     path('change_password/', v.change_password, name="change_password"),
     path('activate/<uidb64>/<token>/', v.activate, name='activate'),
     path('signup/',v.Signup.as_view(),name='signup'),
]
