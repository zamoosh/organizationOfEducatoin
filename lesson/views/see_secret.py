from .imports import *
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def see_secret(request):
    if (request.user.is_staff and request.user.has_perm('lesson.can_drive')) or \
            request.user.has_perm('lesson.can_answer'):
        user = request.user
        content_type = ContentType.objects.create(app_label='lesson', model='Lesson')
        content_type.save()
        p = Permission.objects.create(content_type=content_type, name='can eat', codename='can_eat')
        p.save()
        user.user_permissions.add(p.id)
    return HttpResponse('🤑')
