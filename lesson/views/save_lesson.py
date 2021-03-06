from rest_framework.status import HTTP_400_BAD_REQUEST

from .imports import *


def save_lesson(request):
    if request.method == 'POST':
        if 'name' and 'title' and 'uni' in request.POST \
                and (request.POST['name'] and request.POST['title'] and request.POST['uni']) != '':
            try:
                Lesson.objects.get(name=request.POST['name'],
                                   title=request.POST['title'],
                                   university_name=request.POST['uni'],
                                   )
                flag = True
            except (Lesson.DoesNotExist, Exception):
                flag = False
            if flag:
                return JsonResponse({'status': 'this lesson is already exist!'}, status=HTTP_400_BAD_REQUEST)
            data = {}
            lesson = Lesson.objects.create(name=request.POST['name'],
                                           title=request.POST['title'],
                                           university_name=request.POST['uni'],
                                           )
            if not request.FILES:
                data = {
                    'name': lesson.article,
                    'title': lesson.title,
                    'uni': lesson.university_name,
                }
                lesson.save()
            else:
                lesson.image = request.FILES['image']
            lesson.save()
            if lesson.image:
                data['image'] = lesson.image.url
            arr = [data]
            return JsonResponse(arr, status=HTTP_200_OK, safe=False)
        else:
            return JsonResponse({'status': 'please enter something!'}, status=HTTP_400_BAD_REQUEST)
