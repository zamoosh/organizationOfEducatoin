from .imports import *


def show_article(request):
    context = {'user': request.user}
    return render(request, 'article/articles.html', context)
