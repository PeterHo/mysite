# coding=utf-8
from django.conf.urls import include, url
from django.contrib import admin

__author__ = 'peter'

urlpatterns = [
    url(r'^(?P<list_id>\d+)/$', 'lists.views.view_list', name='view_list'),
    url(r'^new$', 'lists.views.new_list', name='new_list'),
    url(r'^users/(.+)/$', 'lists.views.my_lists', name='my_lists')
]
