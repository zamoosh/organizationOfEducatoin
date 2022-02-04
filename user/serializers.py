from rest_framework import serializers
from . import models as m
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class StudentInfo(serializers.ModelSerializer):
    username = serializers.IntegerField(
        label=_('شماره دانشجویی'),
        error_messages={
            'invalid': 'شماره دانشجویی فقط باید شامل عدد باشد.',
            'required': "این فیلد اجباریست است",
            'blank': 'فیلد شماره دانشجویی نمی‌تواند خالی باشد !',
            "username_exists": 'این شماره دانشجویی در سایت موجود است .',

        }
    )
    email = serializers.EmailField(
        max_length=255,
        error_messages={
            'required': 'فیلد ایمیل اجباریست !',
            'invalid': 'فرمت ایمیل به درستی رعایت نشده !',
            'blank': 'فیلد ایمیل نمی‌تواند خالی باشد !',
            "email_exists": 'این ایمیل در سایت موجود است .',

        }
    )

    class Meta:
        model = m.Student
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'city',
            'state',
            'field',
            'university',
            'profile_image',
        )


    def validate_username(self, username):
        current_user = self.context.get("request").user
        try:
            if current_user.username != username :
                User._default_manager.get(username=username)
                raise serializers.ValidationError(
                    self.fields.get("username").error_messages.get("username_exists"),
                    code='username_exists',
                )
            else:
                return username
        except User.DoesNotExist:
            return username

    def validate_email(self,email):
        current_user = self.context.get("request").user
        try:

            if current_user.email != email:
                User._default_manager.get(email=email)
                raise serializers.ValidationError(
                    self.fields.get("email").error_messages.get("email_exists"),
                    code='email_exists',

                )
            else:
                return email
        except User.DoesNotExist:
            return email


    def validate_profile_image(self,profile_image):
        current_user = self.context.get("request").user
        if profile_image != None :
            return profile_image

        else:
            return current_user.profile_image
