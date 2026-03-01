from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('recommender.urls'))
]

# Add admin panel if enabled
if settings.ADMIN_ENABLED:
    from django.contrib import admin
    urlpatterns.insert(0, path('admin/', admin.site.urls))

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
