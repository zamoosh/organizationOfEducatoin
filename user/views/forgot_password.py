from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import gettext_lazy as _

class ForgotPasswordView(PasswordResetView):
    email_template_name = 'user/password_reset_email.html'
    extra_email_context = None
    form_class = PasswordResetForm
    from_email = 'jafar0650developer@gmail.com'
    html_email_template_name = None
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    template_name = 'user/password_reset_test.html'
    title = _('Password reset')
    token_generator = default_token_generator
