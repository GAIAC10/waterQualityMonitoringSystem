"""waterQualityMonitoringSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from wtoken import views as wtoken_views
app_name='main'

urlpatterns = [
    path('',include('data.urls')),
    path('admin/', admin.site.urls,name='admin'),

    # 试用
    # path('v1/users/', include('usersss.urls')),

    # 进一步试用
    path('tokens', wtoken_views.tokens),
    path('users/', include('users.urls')),
    path('users', user_views.UserViews.as_view()),
    path('index/', include('index.urls')),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
