from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')), #new tuple
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static', #handles uploading of media
        (r'^media/(?P<path>.*)', #change path to ^
         'serve',
         {'document_root': settings.MEDIA_ROOT}), #defined in settings.py
    )

# Deployment step
# set DEBUG to False in settings.py
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
