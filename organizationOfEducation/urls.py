from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from organizationOfEducation import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("user.urls"), name='home'),
    path('lesson/', include("lesson.urls"), name='lesson'),
    path('api_lesson/', include('lesson.apiurls'), name='api_lesson')
]

urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
