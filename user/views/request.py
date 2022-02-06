from .imports import *


def requests(request):
    return render(request, "users/requests.html")
