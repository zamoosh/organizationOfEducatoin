from .imports import *


@csrf_exempt
def save_notification(request):
    if request.method == 'POST':
        if 'description' and 'title' in request.POST:
            try:
                Notifications.objects.get(title=request.POST['title'],
                                          description=request.POST['dec']
                                          )
                flag = True
            except Lesson.DoesNotExist:
                flag = False
            if flag:
                return JsonResponse({'status': 'failed'}, status=HTTP_200_OK)
            notification = Notifications.objects.create(title=request.POST['title'],
                                                        description=request.POST['dec']
                                                        )
            notification.save_lesson()
            return JsonResponse({'status': 'success'}, status=HTTP_200_OK)
        else:
            return HttpResponse('fuck!')
