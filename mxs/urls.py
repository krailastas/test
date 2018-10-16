from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

admin.site.index_title = 'Admin panel'


urlpatterns = [
    url(r'^api/application/', include('files.urls')),
    url(r'^api/profiles/', include('profiles.urls')),
    url(r'grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
]


if settings.DEVELOP_API:
    from rest_framework_swagger.views import get_swagger_view

    schema_view = get_swagger_view(title='API Documentation')

    urlpatterns.append(url(r'^swagger/$', schema_view))


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
