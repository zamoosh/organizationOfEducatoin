from .imports import *


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user:change_password')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'password_change_test.html', {'form': form})