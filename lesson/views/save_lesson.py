from .imports import *


@csrf_exempt
def save_lesson(request):
    if request.method == 'POST':
        if 'name' and 'title' and 'uni' in request.POST:
            try:
                Lesson.objects.get(name=request.POST['name'],
                                   title=request.POST['title'],
                                   university_name=request.POST['uni']
                                   )
                flag = True
            except Lesson.DoesNotExist:
                flag = False
            if flag:
                return JsonResponse({'status': 'failed'}, status=HTTP_200_OK)
            lesson = Lesson.objects.create(name=request.POST['name'],
                                           title=request.POST['title'],
                                           university_name=request.POST['uni']
                                           )
            lesson.save()
            data = {
                'name': lesson.name,
                'title': lesson.title,
                'uni': lesson.university_name
            }
            arr = [data]
            return JsonResponse(arr, status=HTTP_200_OK, safe=False)
        else:
            return HttpResponse('fuck!')
