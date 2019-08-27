# coding:utf-8
# Django settings for moviebar project.
from os.path import dirname, join as join_path
from mongoengine import *
import os

# 连接数据库
connect('wes_wgs', host='10.10.204.15', port=27017,username='wuser', password='berry2012')



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = join_path(dirname(__file__), '../')
SITE_ROOT = os.path.abspath(os.path.dirname(__file__))
# 默认为True的
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    }
}

MONGODB_DATABASES = {
    "default": {
        "NAME": "wes_wgs",
        "HOST": '10.10.204.15',
		"USER":'wuser',
		"PASSWORD":'berry2012',
        "PORT": 27017,
       # "tz_aware": True, # 设置时区
    },
}

ALLOWED_HOSTS = ['*', ]

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-Hans'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_ROOT = os.path.join(SITE_ROOT, 'static')

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    join_path(PROJECT_ROOT, 'static/').replace('\\', '/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '2@^q_03fyoi4o++@1pw%uboymga5g=b#+c&+br0#gv=askf28$'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# 例如：我的 Django 项目的根目录名为“pearl”，ROOT_URLCONF的默认值为“pearl.urls”。
ROOT_URLCONF = 'WebServer.urls'

WSGI_APPLICATION = 'WebServer.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'WebServer',
    'mongoengine',

)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# 文件上传配置
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload/')
MEDIA_URL = '/upload/'
