# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/', include('allauth.urls')),
    url(r'^$', 'mini_chat.core.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
