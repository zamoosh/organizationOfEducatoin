from .imports import *


def add_lesson(request):
    return render(request, 'lesson/lessons.html')
