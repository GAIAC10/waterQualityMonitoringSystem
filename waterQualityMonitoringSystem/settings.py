"""
Django settings for waterQualityMonitoringSystem project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g*(^4@43nwn@%5cg#$+0pc72zq)^-&s-f3o^o#k@8hb(2p^du#'

# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = True
# ALLOWED_HOSTS = []

DEBUG = True
ALLOWED_HOSTS = ['*']
# !!!上线之后!!!
# DEBUG = False
# ALLOWED_HOSTS = ['10.69.26.154']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 添加CORS请求的apps
    'corsheaders',

    'users',
    'wtoken',
    'data',
    'index',

    # 序列化库
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # 在commonmiddleware的前面添加
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'waterQualityMonitoringSystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'waterQualityMonitoringSystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# 法三
X_FRAME_OPTIONS='http://127.0.0.1:8000/index/baidu'

# 本地
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'HOST':'localhost',
        'USER': 'root',
        'PORT':'3306',
        'PASSWORD':'root'
    }
}

# 云服务器
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'Vibe_Water',
#         'HOST':'13.67.56.21',
#         'PORT':'3306',
#         'USER':'root',
#         'PASSWORD':'root'
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

# 关闭时区功能后，数据库存储时间时，按照TIME_ZONE时区进行存储
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# !!!上线
STATIC_ROOT='/home/yoko/waterQualityMonitoringSystem_static/static'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CORS全部都可以进
CORS_ORIGIN_ALLOW_ALL=True

# CORS允许的请求方法
CORS_ALLOW_METHODS = (
                'DELETE',
                'GET',
                'OPTIONS',
                'PATCH',
                'POST',
                'PUT',
                )

# CORS允许的请求头
CORS_ALLOW_HEADERS = (
                'accept-encoding',
                'authorization',
                'content-type',
                'dnt',
                'origin',
                'user-agent',
                'x-csrftoken',
                'x-requested-with',
            )

# 上传的头像保存在该路径中
# MEDIA_URL和MEDIA_ROOT需要手动将两者绑定在一起
# 1.新建media文件夹 2.在主urls中配置
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

JWT_TOKEN_KEY='123456'

# django-redis配置
CACHES = {
    "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            # 默认是0库;redis://127.0.0.1:6379/1,表示2库
            "LOCATION": "redis://127.0.0.1:6379/1",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                # "PASSWORD":'123456',
            }
        }
}
# 方法一：cache.set/get
# 具备序列化和反序列化
# 方法二：
# from django_redis import get_redis_connection
# r=get_redis_connection()
# r.redis命令
# 方法三：
# from django.views.decorators.cache import cache_page
# 装饰器->cache_page(60)


ACCOUNTSID='8aaf07087a331dc7017ad92a25cb33cb'
ACCOUNTTOKEN='895fc86f9cec4525b9fedaf849e12d41'
APPID='8aaf07087a331dc7017ad92a26c433d1'
TEMPLATEID='1'
