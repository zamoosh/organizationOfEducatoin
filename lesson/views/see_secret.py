from .imports import *


def see_secret(request):
    if (request.user.is_staff and request.user.has_perm('lesson.can_drive')) or \
            request.user.has_perm('lesson.can_answer'):
        user = request.user
        p = Permission.objects.get(name='Can answer question')
        user.user_permissions.add(p)
        user.save()
        print(user.get_user_permissions())
    return HttpResponse('🤑')
