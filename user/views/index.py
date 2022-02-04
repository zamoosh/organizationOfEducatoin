from .imports import *


def index(request):
    return render(request, 'index.html')
