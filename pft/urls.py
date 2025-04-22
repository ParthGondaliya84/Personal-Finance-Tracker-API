from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularAPIView,
    SpectacularRedocView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('apps.user.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('schema', SpectacularAPIView.as_view(), name='schema'),
        path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]

    urlpatterns += static(settings.MEDIA_URL, doccument_root=settings.MEDIA_ROOT)