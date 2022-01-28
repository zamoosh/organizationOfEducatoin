from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView
)
from ..forms import ForgotPasswordForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


UserModel = get_user_model()


class ForgotPasswordView(PasswordResetView):
    email_template_name = 'user/password_reset/password_reset_email.html'
    form_class = ForgotPasswordForm
    subject_template_name = 'user/password_reset/password_reset_subject.txt'
    success_url = reverse_lazy('user:password_reset_done')
    template_name = 'user/password_reset/password_reset_test.html'
    title = _('بازیابی رمز عبور')
    token_generator = default_token_generator

class ForgotPasswordDoneView(PasswordResetDoneView):
    template_name = 'user/password_reset/password_reset_done.html'
    title = _('لینک بازیابی گذرواژه ارسال شد')


class ForgotPasswordConfirmView(PasswordResetConfirmView):
    #################################################################################################################3
    form_class = SetPasswordForm
    # post_reset_login = False
    # post_reset_login_backend = None
    reset_url_token = 'set-password'
    success_url = reverse_lazy('user:password_reset_complete')
    template_name = 'user/password_reset/password_reset_confirm.html'
    title = _('رمز عبور جدید را وارد کنید')
    token_generator = default_token_generator


class ForgotPasswordCompleteView(PasswordResetCompleteView):
    template_name = 'user/password_reset/password_reset_complete.html'
    title = _('رمز عبور با موفقیت تغییر کرد')






