from .imports import *


def lesson_directory_name(instance):
    current_date = datetime.date.today()
    year = current_date.year
    month = current_date.month
    day = current_date.day
    j = jdatetime.date.fromgregorian(day=day, month=month, year=year, locale='fa_IR')
    day = j.day
    month = j.month
    year = j.year
    return '%s/%s/%s/%s/%s' % ('lesson', instance.name, year, month, day)


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
            lesson.save()
            if not request.FILES:
                data = {
                    'name': lesson.name,
                    'title': lesson.title,
                    'uni': lesson.university_name,
                }
            else:
                img = request.FILES['image']
                path = settings.MEDIA_ROOT
                path += lesson_directory_name(lesson)
                file = FileSystemStorage(location=path)
                lesson.image = file.save(img.name, img)
                data['image'] = file.location
            lesson.save()

            arr = [data]
            return JsonResponse(arr, status=HTTP_200_OK, safe=False)
        else:
            return JsonResponse({'status': 'empty'}, status=HTTP_200_OK)
