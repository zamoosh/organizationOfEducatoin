from .imports import *
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def see_secret(request):
    if (request.user.is_staff and request.user.has_perm('lesson.can_drive')) or \
            request.user.has_perm('lesson.can_answer'):
        user = request.user
        content_type = ContentType.objects.get_or_create(app_label='lesson', model='Lesson')
        content_type[0].save() if content_type[1] else None
        permission = Permission.objects.get_or_create(content_type=content_type[0], name='can sleep',
                                                      codename='can_sleep')
        permission[0].save() if permission[1] else None
        user.user_permissions.add(permission[0].id)
        user.save()
        print(user.user_permissions.all())
    return HttpResponse('🤑')
