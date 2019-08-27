#coding:utf-8
import urllib2
import json
import re
from django import forms
from django.contrib import admin, messages
from django.template.response import TemplateResponse

from . import models

#id 必须用小写，我也是醉了。
#然后 .join(obj.tags.values_list('TieBa_Content', flat=True)) 里面的内容好像不能为ID，否则会报错


