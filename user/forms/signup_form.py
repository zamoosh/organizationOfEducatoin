from django.contrib.auth.forms import UserCreationForm
from ..models import Student
from django import forms
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from ..validators import validate_email
User = get_user_model()




class SignupForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _('پسورد های وارد شده یکسان نمی‌باشند.'),
        "username_exists": _('این شماره دانشجویی در سایت موجود است .'),
        "email_exists": _('این ایمیل در سایت موجود است .'),
    }
    username = forms.IntegerField(
        label=_("شماره دانشجویی"),
        error_messages={
            'required': 'فیلد شماره دانشجویی اجباریست !',
            'invalid': 'فرمت شماره دانشجویی به درستی رعایت نشده !'
        }
    )
    email = forms.EmailField(
        label=_("ایمیل"),
        max_length=255,
        error_messages={
            'required': 'فیلد ایمیل اجباریست !',
            'invalid' : 'فرمت ایمیل به درستی رعایت نشده !'
        }
    )
    password1 = forms.CharField(
        label=_("رمز عبور"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
        error_messages={
            'required': 'فیلد رمز عبور اجباریست !',
        }
    )
    password2 = forms.CharField(
        label=_("تکرار رمز عبور"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        error_messages={
            'required': 'فیلد تکرار رمز عبور اجباریست !',
        }
    )

    class Meta:
        model = Student
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def clean_username(self):
        username = self.cleaned_data.get("username")

        try:
            user = User._default_manager.get(username=username)
            if not user.is_active:
                user.delete()
            else:
                raise forms.ValidationError(
                    self.error_messages['username_exists'],

                    code='username_exists',

                )
        except User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data.get("email")

        try:
            User._default_manager.get(email=email)
            raise forms.ValidationError(
                self.error_messages['email_exists'],

                code='email_exists',

            )
        except User.DoesNotExist:
            return email
