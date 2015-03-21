from django.conf.urls import patterns, url

urlpatterns = patterns('userpref.views',
    url(r'^$', 'view', name='userpref_view'),
    url(r'^edit', 'edit', name='userpref_edit'),
)