from django.shortcuts import redirect
from django.contrib.auth import logout


def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("user:signin")
