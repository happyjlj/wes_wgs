# -*- coding: utf-8 -*-

from django import forms
# 文件上传表单
class FileForm(forms.Form):
    fileupload = forms.FileField(label=u"数据文件")
