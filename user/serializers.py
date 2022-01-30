from rest_framework import serializers
from . import models as m

class StudentInfo(serializers.ModelSerializer):
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
