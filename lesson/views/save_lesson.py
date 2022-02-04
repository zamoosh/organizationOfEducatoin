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
                return JsonResponse({'status': 'failed'}, status=HTTP_200_OK)
            data = {}
            lesson = Lesson.objects.create(name=request.POST['name'],
                                           title=request.POST['title'],
                                           university_name=request.POST['uni'],
                                           )
            if not request.FILES:
                data = {
                    'name': lesson.name,
                    'title': lesson.title,
                    'uni': lesson.university_name,
                }
                lesson.save()
            else:
                img = request.FILES['image']
                path = settings.MEDIA_ROOT
                path += directory_name(lesson, filename=None)
                file = FileSystemStorage(location=path)
                lesson.image = file.save(img.name, img)
                data['image'] = file.location
            lesson.save()
            arr = [data]
            return JsonResponse(arr, status=HTTP_200_OK, safe=False)
        else:
            return JsonResponse({'status': 'empty'}, status=HTTP_200_OK)
