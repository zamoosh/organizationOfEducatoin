from .imports import *


def lesson(request):
    return render(request, "lesson/lesson.html")
