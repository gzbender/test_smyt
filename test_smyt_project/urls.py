from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'test_smyt.views.index.index', name='index'),
    url(r'^api/', include(patterns('',
        url(r'^objects/(?P<model>\w+)/$', 'test_smyt.views.api.objects', name='objects'),
        url(r'^objects/(?P<model>\w+)/new$', 'test_smyt.views.api.create_object', name='create_object'),
        url(r'^objects/(?P<model>\w+)/(?P<pk>\d+)/edit$', 'test_smyt.views.api.update_object', name='update_object'),
    ))),

    url(r'^admin/', include(admin.site.urls)),
)
