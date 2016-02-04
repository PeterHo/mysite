# coding=utf-8
from django.conf.urls import include, url
from django.contrib import admin

__author__ = 'peter'

urlpatterns = [
    url(r'^$', 'scoreboard.views.scores', name='scores'),
]
