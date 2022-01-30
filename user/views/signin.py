from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from ..forms import (
    SigninForm,
    SignupForm ,
    ForgotPasswordForm,
    )
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import get_user_model

User = get_user_model()


class Signin(LoginView):
    form_class = SigninForm
    next_page = 'test'
    template_name = 'login/login.html'


    def form_invalid(self, form):
        username = self.request.POST.get('username')
        user = User.objects.get_object_or_nothing(username=username)
        if user!=None and not user.is_active:
            mail_subject = "لطفا اکانت خود را فعال نمایید"
            current_site = get_current_site(self.request)
            message = render_to_string(
                'user/account_activation_email.html',
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user)
                }
            )
            to_email = user.email
            email = EmailMessage(
                mail_subject,
                message,
                to=[to_email]
            )
            email.send()
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signin_form'] = self.get_form()
        context['signup_form'] = SignupForm
        context['forgot_form'] = ForgotPasswordForm
        context['signup'] = False
        context['signin'] = True
        context['forgot'] = False

        return context
