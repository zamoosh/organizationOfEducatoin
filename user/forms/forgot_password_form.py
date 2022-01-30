from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext_lazy as _
from django import forms
from .. import password_validation


class ForgotPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("ایمیل خود را وارد کنید"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': "input"}),
        error_messages={
            'required': 'فیلد ایمیل اجباریست !',
            'invalid': 'فرمت ایمیل به درستی رعایت نشده !'
        }
    )


class PutPasswordForm(SetPasswordForm):
    error_messages = {
        'password_mismatch': _(
            'پسورد های وارد شده یکسان نمی‌باشند.'
        ),
        'password_incorrect': _(
            "رمز عبور فعلی ضما صحیح نمی‌باشد . لطفا دوباره تلاش نمایید ."
        ),
    }
    new_password1 = forms.CharField(
        label=_("رمز عبور جدید"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': "input"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
        error_messages={
            'required': _(
                "این فیلد اجباریست است"
            )
        }
    )
    new_password2 = forms.CharField(
        label=_("تکرار رمز عبور جدید"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': "input"}),
        error_messages={
            'required': _(
                "این فیلد اجباریست است"
            )
        }
    )
