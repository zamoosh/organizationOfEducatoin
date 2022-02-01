from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated

from .. import serializers as s
from .. import models as m
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.authentication import SessionAuthentication
from django.views.generic import CreateView
from ..forms import (
    SignupForm,
    SigninForm,
    ForgotPasswordForm,
)
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.shortcuts import HttpResponse, redirect


class StudentProfileAPI(viewsets.ViewSet):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer, BrowsableAPIRenderer]
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        queryset = m.Student.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = s.StudentInfo(user)
        data = {'serializer': serializer}
        # data.update(serializer.data)
        if request.accepted_renderer.format == 'json' or request.accepted_renderer.format == 'api':
            return Response(data=serializer.data)
        else:
            return Response(data=data, template_name='user/tests.html')

    def partial_update(self, request, pk=None):
        queryset = m.Student.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        a=request.data['email']
        img=request.data['profile_image']
        if request.data['email'] != user.email:
            current_site = get_current_site(request)
            mail_subject = "لطفا اکانت خود را فعال نمایید"
            to_email = request.data['email']
            message = render_to_string(
                'user/change_email.html',
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'new_email': urlsafe_base64_encode(force_bytes(to_email)),
                    'token': default_token_generator.make_token(user)
                }
            )
            email = EmailMessage(
                mail_subject,
                message,
                to=[to_email]
            )
            serializer = s.StudentInfo(instance=user, data=request.data)
            serializer.is_valid(raise_exception=True)
            email.send()

            data = {'serializer': serializer,'jafar':a}
            if request.accepted_renderer.format == 'json' or request.accepted_renderer.format == 'api':
                return Response(data=serializer.data)
            else:
                return Response(data=data, template_name='user/tests.html')
        serializer = s.StudentInfo(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        data ={'serializer': serializer , 'img':img}
        if request.accepted_renderer.format == 'json' or request.accepted_renderer.format == 'api':
            return Response(data=serializer.data)
        else:
            return Response(data=data, template_name='user/tests.html')


def change_email(request, uidb64, new_email, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = m.Student.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, m.Student.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        email = force_str(urlsafe_base64_decode(new_email))
        user.email = email
        user.save()
        return redirect('test')
    else:
        return HttpResponse('user/account_activation_invalid.html')

