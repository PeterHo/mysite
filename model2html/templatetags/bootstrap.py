# coding=utf-8
from __future__ import print_function, unicode_literals, absolute_import
from bootstrap3.templatetags import bootstrap3
from django.shortcuts import render
from django.template.loader import render_to_string

from .model2html import register

__author__ = 'peter'

MODEL2HTML_BOOTSTRAP_SETTINGS = {
    'horiz_label_class': 'col-xs-3',
    'horiz_field_class': 'col-xs-9',
}


def render_template_file(file_name, ctx):
    template_file = "model2html/bootstrap/" + file_name + ".html"
    ctx['settings'] = MODEL2HTML_BOOTSTRAP_SETTINGS
    return render_to_string(template_file, context=ctx)
    # return render(None, template_file, ctx).content


###############################################################################
# django-bootstrap3的封装
###############################################################################
# 封装django-bootstrap3的bootstrap_field方法,加入默认参数
bootstrap_field_default_param = {
    'layout': 'horizontal',
    'size': 'sm',
    'set_required': False,
}


@register.simple_tag
def bootstrap_field(*args, **kwargs):
    for (k, v) in bootstrap_field_default_param.items():
        if k not in kwargs:
            kwargs[k] = v
    return bootstrap3.bootstrap_field(*args, **kwargs)


@register.simple_tag
def bootstrap_button(*args, **kwargs):
    return bootstrap3.bootstrap_button(*args, **kwargs)


###############################################################################
# Bootstrap 通用代码生成
###############################################################################
# 生成header
@register.simple_tag
def bootstrap_header(text):
    ctx = {'text': text}
    return render_template_file("header", ctx)


# 生成radio
@register.simple_tag
def bootstrap_radio(field, **kwargs):
    ctx = kwargs
    ctx['field'] = field
    return render_template_file("radio", ctx)


# 生成select
@register.simple_tag
def bootstrap_select(field, **kwargs):
    ctx = kwargs
    ctx['field'] = field
    ctx['id'] = field.auto_id
    ctx['name'] = field.name
    ctx['label'] = field.label
    if hasattr(field.field, 'choices'):
        ctx['choices'] = field.field.choices
    return render_template_file("select", ctx)


# 生成textarea
@register.simple_tag
def bootstrap_textarea(field, **kwargs):
    ctx = kwargs
    ctx['field'] = field
    ctx['id'] = field.auto_id
    ctx['name'] = field.name
    ctx['label'] = field.label
    ctx['max_length'] = field.field.max_length
    if 'place_holder' not in ctx:
        ctx['place_holder'] = field.field.widget.attrs['placeholder']
        # ctx['place_holder'] = field.label
    return render_template_file("textarea", ctx)


# 头像上传
@register.simple_tag
def bootstrap_head_portrait_upload(field, img_type, **kwargs):
    ctx = kwargs
    ctx['field'] = field
    ctx['img_type'] = img_type
    return render_template_file("head_portrait_upload", ctx)


# 上传多张照片
@register.simple_tag
def bootstrap_imgs_upload(**kwargs):
    return render_template_file("imgs_upload", kwargs)


# 图片的编辑窗口
# 注意这个方法会生成form表单,因此不能放在form块里面
@register.simple_tag
def bootstrap_imgs_edit_modal(**kwargs):
    return render_template_file("imgs_edit_modal", kwargs)


# Carousel
@register.simple_tag
def bootstrap_carousel(**kwargs):
    return render_template_file("carousel", kwargs)


###############################################################################
# Bootstrap 模块相关代码生成
###############################################################################
# 生成宠物价格表单项
@register.simple_tag
def bootstrap_pet_price(field, **kwargs):
    ctx = kwargs
    ctx['field'] = field
    ctx['id'] = field.auto_id
    ctx['name'] = field.name
    ctx['label'] = field.label
    ctx['place_holder'] = '请输入价格'
    return render_template_file("pet_price", ctx)


# 生成选择自己宠物按钮组
@register.simple_tag
def bootstrap_select_my_pet(field, **kwargs):
    ctx = kwargs
    return render_template_file("select_my_pet", ctx)


# 生成特色服务按钮组
@register.simple_tag
def bootstrap_special_service(field, **kwargs):
    ctx = kwargs
    ctx['field'] = field
    return render_template_file("special_service", ctx)

