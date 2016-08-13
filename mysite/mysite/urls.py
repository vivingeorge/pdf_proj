from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', include('indee.urls')),
    url(r'^indee/', include('indee.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
