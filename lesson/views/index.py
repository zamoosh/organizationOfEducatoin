from .imports import *


def index(request):
    context = {
        'lessons': Lesson.objects.all(),
        'articles': Article.objects.all(),
        'notifications': Notifications.objects.all(),
    }
    return render(request, 'index.html', context)
