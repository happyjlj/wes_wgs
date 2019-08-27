# coding:utf-8
from django import VERSION

if VERSION[0:2] > (1, 9):
    from django.conf.urls import url, include
elif VERSION[0:2] > (1, 3):
    from django.conf.urls import patterns, url, include
else:
    from django.conf.urls.defaults import patterns, url, include

# from django.conf.urls import patterns, include, url
from django.contrib import admin
import os

from . import views

# from dbs import views

SITE_ROOT = os.path.abspath(os.path.dirname(__file__))

admin.autodiscover()
'''
urlpatterns = patterns('',

    #依然是Django默认的管理员的界面                 
    url(r'^admin/', include(admin.site.urls)),
                       
    #首页的URL，生成的界面在view.py里面的Home函数
    url(r'^$', views.home, name='home'),

    # 查看其余参数界面
    url(r'^homechild/$', views.homechild),

)
'''
if VERSION[0:2] > (1, 9):
    urlpatterns = [
        # 依然是Django默认的管理员的界面
        url(r'^admin/', include(admin.site.urls)),

        # 首页的URL，生成的界面在view.py里面的Home函数
        # url(r'^$', views.home, name='home'),
        url(r'^$', views.result, name='result'),

        # 查看其余参数界面
        # url(r'^homechild/$', views.homechild),
        url(r'^cartgram/$', views.cartgram),
        url(r'^single/$', views.single),
        # EXCEL文件上传统计
        url(r'^xlsStat$', views.xlsStat),
        url(r'^gettables$', views.gettables),
        # 开发使用
        url(r'^test$', views.test)
    ]
else:
    urlpatterns = patterns('',
                           # 依然是Django默认的管理员的界面
                           url(r'^admin/', include(admin.site.urls)),

                           # 首页的URL，生成的界面在view.py里面的Home函数
                           # url(r'^$', views.home, name='home'),
                           url(r'^$', views.result, name='result'),
                           # 查看其余参数界面
                           # url(r'^homechild/$', views.homechild),
                           url(r'^cartgram/$', views.cartgram),
                           url(r'^single/$', views.single),

                           # EXCEL文件上传统计
                           url(r'^xlsStat$', views.xlsStat),
                           url(r'^gettables$', views.gettables),
                           # 开发使用
                           url(r'^test$', views.test)

                           )
