from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'socialdoctor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'social.views.home', name='home'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^register/$', 'social.views.register', name='register'),


    url(r'^person/(?P<person_id>\d+)/$', 'social.views.person', name='person'),

    url(r'^person/(?P<person_id>\d+)/send_feedback/$', 'social.views.send_feedback', name='send_feedback'),

    url(r'^admin/', include(admin.site.urls)),
]

