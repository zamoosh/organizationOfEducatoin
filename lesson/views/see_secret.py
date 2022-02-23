from .imports import *


def see_secret(request):
    if (request.user.is_staff and request.user.has_perm('lesson.can_drive')) or \
            request.user.has_perm('lesson.can_answer'):
        user = request.user
    return HttpResponse('🤑')
