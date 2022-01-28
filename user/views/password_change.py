from django.contrib.auth.views import PasswordChangeView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from ..forms import ChangePasswordForm

# def change_password(request):
#     if request.method == 'POST'
#         form = ChangePasswordForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('user:change_password')
#     else:
#         form = ChangePasswordForm(request.user)
#     return render(request, 'user/password_change_test.html', {'form': form})

class ChangePassword(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('test')
    template_name = 'user/password_change_test.html'
    title = _('تغییر رمز عبور')