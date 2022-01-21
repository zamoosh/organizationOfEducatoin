from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django import forms


class SigninForm(AuthenticationForm):
    username = forms.IntegerField(
        label=_("شماره دانشجویی"),
        widget=forms.TextInput(attrs={'autofocus': True}),
        error_messages={
            'invalid': _('شماره دانشجویی فقط باید شامل عدد باشد.'),
        }
    )
    password = forms.CharField(
        label=_("رمز عبور"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    error_messages = {
        'invalid_login': _(
            "لطفا شماره دانشجویی و رمز عبور را به درستی وارد کنید."
        ),
        'inactive': _(
            "این اکانت غیر فعال است. لطفا ابتدا آن را فعال کنید."
        ),
    }
