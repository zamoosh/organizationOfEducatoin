from django.contrib.auth.views import PasswordChangeView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from ..forms import ChangePasswordForm



class ChangePassword(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('test')
    template_name = 'user/password_change_test.html'
    title = _('تغییر رمز عبور')