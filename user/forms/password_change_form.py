from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django import forms
from .. import password_validation


class ChangePasswordForm(PasswordChangeForm):
    error_messages = {
        'password_mismatch': _('پسورد های وارد شده یکسان نمی‌باشند.'),
        'password_incorrect': _("رمز عبور فعلی ضما صحیح نمی‌باشد . لطفا دوباره تلاش نمایید ."),
    }
    new_password1 = forms.CharField(
        label=_("رمز عبور جدید"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("تکرار رمز عبور جدید"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    old_password = forms.CharField(
        label=_("رمز عبور فعلی"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )
