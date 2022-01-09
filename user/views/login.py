from .imports import *


def login(request):
    return render(request, "login.html")
