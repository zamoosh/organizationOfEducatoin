from .imports import *


def change_password(request):
    form = ChangePasswordForm(request.user)
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('user:change_password')
    return render(request, 'user/password_change_test.html', {'form': form})