from .imports import *


def save_article(request):
    if request.method == 'POST':
        if ('name' and 'title' and 'subject' and 'dec' in request.POST) and (
                request.POST['name'] and
                request.POST['title'] and
                request.POST['uni'] and
                request.POST['subject'] and
                request.POST['dec']
        ) != '':
            try:
                Article.objects.get(name=request.POST['name'],
                                    title=request.POST['title'],
                                    subject=request.POST['subject'],
                                    )
                flag = True
            except (Article.DoesNotExist, Exception):
                flag = False
            if flag:
                return JsonResponse({'status': 'failed'}, status=HTTP_200_OK)
            data = {}
            article = Article.objects.create(name=request.POST['name'],
                                             title=request.POST['title'],
                                             subject=request.POST['subject'],
                                             description=request.POST['dec']
                                             )
            if not request.FILES:
                data = {
                    'name': article.name,
                    'title': article.title,
                    'subject': article.subject,
                    'dec': article.description
                }
                article.save()
            else:
                article_file = request.FILES['file']
                path = settings.MEDIA_ROOT
                path += directory_name_article(Article, filename=None)
                file = FileSystemStorage(location=path)
                Article.file = file.save(article_file.name, article_file)
                data['file'] = file.location
            article.save()
            arr = [data]
            return JsonResponse(arr, status=HTTP_200_OK, safe=False)
        else:
            return JsonResponse({'status': 'empty'}, status=HTTP_200_OK)
