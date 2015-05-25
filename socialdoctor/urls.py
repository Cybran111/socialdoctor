from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'socialdoctor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'social.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout",),
    # url('^', include('django.contrib.auth.urls')),
    url(r'^register/$', 'social.views.register', name='register'),


    url(r'^person/(?P<person_id>\d+)/$', 'social.views.person', name='person'),
    url(r'^person/search/(?P<person_id>\s+)/$', 'social.views.search', name='search'),

    url(r'^person/(?P<person_id>\d+)/messages/$', 'social.views.messages', name='messages'),
    url(r'^person/notificatons/$', 'social.views.notifications', name='notifications'),

    url(r'^person/(?P<person_id>\d+)/follow$', 'social.views.person_follow', name='follow'),
    url(r'^person/(?P<person_id>\d+)/unfollow$', 'social.views.person_unfollow', name='unfollow'),

    url(r'^person/(?P<person_id>\d+)/send_feedback/$', 'social.views.send_feedback', name='send_feedback'),
    url(r'^person/search/$', 'social.views.search', name='search'),
    url(r'^person/search/$', 'social.views.search', name='search'),
    url(r'^person/search/doctors/$', 'social.views.search_doctors', name='search_doctors'),
    url(r'^person/search/patients/$', 'social.views.search_patients', name='search_patients'),

    url(r'^admin/', include(admin.site.urls)),
]

