# coding=utf-8
from __future__ import print_function, unicode_literals, absolute_import
from django import template

__author__ = 'peter'

register = template.Library()

from .jqm import *
from .bootstrap import *

