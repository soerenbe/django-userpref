from django.conf.urls import patterns, include, url
from django.contrib import admin
import userpref.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^settings/', include(userpref.urls)),
)
