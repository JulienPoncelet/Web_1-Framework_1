from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app00.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^createaccount/', 'createaccount.views.user', name='createaccount'),
)
