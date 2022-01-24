import form as form
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView
from ..forms import SignupForm
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model

User = get_user_model()


class Signup(CreateView):
    form_class = SignupForm
    template_name = "user/signup_test.html"

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = "اکانت خود را فعال نمایید ."
        message = render_to_string(
            'user/account_activation_email.html',
            {
                'user': user,
                'domain': '127.0.0.1:8000',
                'admin': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            }
        )
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject,
            message,
            to=[to_email]
        )
        email.send()
        return HttpResponse("لطفا اکانت خود را فعال نمایید")



def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('test')
    else:
        return HttpResponse('user/account_activation_invalid.html')
