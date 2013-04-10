from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from haikus.views import homepage, user_page
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', homepage, name='homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^calculator/$', 'calculator.views.calculator'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),
    url(r'^feedback/$', 'feedback.views.contact_form', name='contact-form'),
    url(r'^(?P<username>\w+)/$', user_page, name='user-page'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
