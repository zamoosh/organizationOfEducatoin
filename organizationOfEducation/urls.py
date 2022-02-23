from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from organizationOfEducation import settings
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('schema/', get_schema_view(
        title="organization of education",
        description="API for all objects",
        version="1.0.0"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls'), name='home'),
    path('lesson/', include('lesson.urls'), name='lesson'),
    path('article/', include('article.urls'), name='article'),

    path('api-auth/', include('rest_framework.urls'), name='api auth'),

    path('api_lesson/', include('lesson.apiurls'), name='api lesson'),
    path('api_notification/', include('lesson.apiurls'), name='api notification'),
    path('api_article/', include('article.apiurls'), name='api article'),
    path('api_feedback/', include('feedback.apiurls'), name='api feedback'),
    path('mohammad/', include('lesson.urls'), name='mohammad')

]

urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
