from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from organizationOfEducation import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("user.urls"), name='home'),
    path('lesson/', include("lesson.urls"), name='lesson'),
    path('article/', include("article.urls"), name='article'),
    path('api_lesson/', include('lesson.apiurls'), name='api lesson'),
    path('api_notification/', include('lesson.apiurls'), name='api notification'),
    path('api_article/', include('article.apiurls'), name='api article'),
    path('api_feedback/', include('feedback.apiurls'), name='api feedback'),
    path('mohammad/', include('lesson.urls'), name='mohammad')

]

urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
