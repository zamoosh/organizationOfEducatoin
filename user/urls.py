from django.urls import path, include
from . import views as v
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('api', v.StudentProfileAPI, basename='profile')
app_name = "user"
urlpatterns = [
     path('',include(router.urls)),
     path('email/<uidb64>/<new_email>/<token>/', v.change_email, name='change_email'),
     path('signin/', v.Signin.as_view(), name="signin"),
     path('signout/', v.sign_out, name="signout"),
     path('change_password/', v.ChangePassword.as_view(), name="change_password"),
     path('activate/<uidb64>/<token>/', v.activate, name='activate'),
     path('signup/',v.Signup.as_view(),name='signup'),
     path('password_reset/', v.ForgotPasswordView.as_view(), name='password_reset'),
     path('password_reset/done/', v.ForgotPasswordDoneView.as_view(), name='password_reset_done'),
     path('reset/<uidb64>/<token>/', v.ForgotPasswordConfirmView.as_view(), name='password_reset_confirm'),
     path('reset/done/', v.ForgotPasswordCompleteView.as_view(), name='password_reset_complete'),
]