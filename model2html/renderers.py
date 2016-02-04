# coding=utf-8
from __future__ import print_function, unicode_literals, absolute_import
from django.forms import RadioSelect
from django.utils.safestring import mark_safe

__author__ = 'peter'


# 重载RadioSelect的render方法实现radio的横向排列
class HorizRadioRenderer(RadioSelect.renderer):
    def render(self):
        return mark_safe('\n'.join(['%s\n' % w for w in self]))
