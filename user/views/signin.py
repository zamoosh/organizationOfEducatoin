from .imports import *


def sign_in(request):
    form = SigninForm()
    # request.POST or None, request.FILES or None
    if request.method == "POST":
        form = SigninForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user=user)
                return redirect("user:test")
    return render(request, template_name="signin_test.html" , context={"form":form})
