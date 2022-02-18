from .imports import *


def detail_lesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    context = {'lesson': lesson}
    return render(request, 'lesson/lesson.html', context)
