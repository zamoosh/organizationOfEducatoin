from lesson.models import Lesson
from .imports import *


def login(request):
    context = {
        'objects': Lesson.objects.all()
    }
    return render(request, "login/login.html")
