# coding=utf-8
from django.conf.urls import url

__author__ = 'peter'

urlpatterns = [
    url(r'^login$', 'accounts.views.persona_login', name='persona_login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout')
]
