# coding=utf-8
from __future__ import print_function, unicode_literals, absolute_import
from django.forms.fields import CharField
from django.shortcuts import render

from .model2html import register

__author__ = 'peter'


def render_template_file(file_name, ctx):
    template_file = "model2html/jqm/" + file_name + ".html"
    return render(None, template_file, ctx).content


###############################################################################
# jQuery Mobile 代码生成
###############################################################################
@register.simple_tag
def jqm_header(text):
    ctx = {'text': text}
    return render_template_file("header", ctx)


@register.simple_tag
def jqm_input(field, **kwargs):
    ctx = kwargs
    ctx['id'] = field.auto_id
    ctx['name'] = field.name
    ctx['label'] = field.label

    if isinstance(field.field, CharField):
        ctx['max_length'] = field.field.max_length

    if 'place_holder' not in ctx:
        ctx['place_holder'] = field.label

    return render_template_file("input", ctx)


@register.simple_tag
def jqm_textarea(field, **kwargs):
    ctx = kwargs
    ctx['id'] = field.auto_id
    ctx['name'] = field.name
    ctx['label'] = field.label

    if isinstance(field.field, CharField):
        ctx['max_length'] = field.field.max_length

    if 'place_holder' not in ctx:
        ctx['place_holder'] = field.label

    return render_template_file("textarea", ctx)


@register.simple_tag
def jqm_radio(field, **kwargs):
    ctx = kwargs
    ctx['id'] = field.auto_id
    ctx['name'] = field.name
    ctx['label'] = field.label
    ctx['choices'] = field.field.choices
    return render_template_file("radio", ctx)


@register.simple_tag
def jqm_select(field, **kwargs):
    ctx = kwargs
    ctx['id'] = field.auto_id
    ctx['name'] = field.name
    ctx['label'] = field.label
    if hasattr(field.field, 'choices'):
        ctx['choices'] = field.field.choices
    return render_template_file("select", ctx)


# 生成宠物价格表单项
@register.simple_tag
def jqm_pet_price(field, **kwargs):
    ctx = kwargs
    ctx['id'] = field.auto_id
    ctx['name'] = field.name
    ctx['label'] = field.label
    ctx['place_holder'] = '请输入价格'
    return render_template_file('pet_price', ctx)


# 生成特色服务按钮组
@register.simple_tag
def jqm_special_service(**kwargs):
    ctx = kwargs
    ctx['service_text'] = {
        'service1': '特色1',
        'service2': '特色2',
        'service3': '特色3',
        'service4': '特色4',
        'service5': '特色5',
        'service6': '特色6',
        # 'service7': '特色7',
        # 'service8': '特色8',
    }
    return render_template_file('special_service', ctx)
