from .imports import *


def sign_out(request):
    if request.user.is_authenticated :
        logout(request)
    return redirect("user:signin")

