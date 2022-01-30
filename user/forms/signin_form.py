from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

class SigninForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            "لطفا شماره دانشجویی و رمز عبور را به درستی وارد کنید."
        ),
        'inactive': _(
            "این اکانت غیر فعال است. لینک فعال سازی مجدد برای شما ایمیل شد .اگر ایمیل خود را اشتباه وارد کرده اید مجدد ثبت نام کنید ."
        ),
    }
    username = forms.IntegerField(
        label=_("شماره دانشجویی"),
        widget=forms.TextInput(attrs={'autofocus': True, 'class': "input"}),
        error_messages={
            'invalid': _(
                'شماره دانشجویی فقط باید شامل عدد باشد.'
            ),
            'required': _(
                "این فیلد اجباریست است"
            )
        }
    )
    password = forms.CharField(
        label=_("رمز عبور"),
        # strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': "input"}),
        error_messages={
            'required': _(
                "این فیلد اجباریست است"
            )
        }
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")

        try:
            user = User._default_manager.get(username=username)
            if not user.is_active:
                raise forms.ValidationError(
                    self.error_messages['inactive'],
                    code='inactive',
                )

            else:
                return username
        except User.DoesNotExist:
            raise forms.ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
            )
