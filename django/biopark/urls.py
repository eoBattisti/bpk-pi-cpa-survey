"""biopark URL Configuration."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from biopark import views


urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/", include("biopark.api_urls")),
    path("eixos/", include("axis.urls")),
    path("perguntas/", include('questions.urls'))
    
]


handler400 = views.Handler400View.as_view()
handler403 = views.Handler403View.as_view()
handler404 = views.Handler404View.as_view()
handler500 = views.Handler500View.as_view()


if settings.DEBUG:
    # Getting media files for debug environment.
    urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns

    # Getting django-debug-toolbar assets.
    urlpatterns = [path('__debug__/', include('debug_toolbar.urls'))] + urlpatterns
