from .imports import *


def show_article(request):
    context = {
        'user': request.user,
        'articles': Article.objects.all(),
    }
    return render(request, 'article/articles.html', context)
