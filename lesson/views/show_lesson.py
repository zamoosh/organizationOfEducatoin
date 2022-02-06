from .imports import *


def show_lesson(request):
    return render(request, 'lesson/lessons.html')
