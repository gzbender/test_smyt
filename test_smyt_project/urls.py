from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'test_smyt.views.index', name='index'),
    url(r'^object-list/(?P<model>\w+)/$', 'test_smyt.views.object_list', name='object_list'),

    url(r'^admin/', include(admin.site.urls)),
)
