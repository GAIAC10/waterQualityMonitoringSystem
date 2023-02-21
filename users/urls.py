from django.urls import path
from . import views
app_name='users'
urlpatterns = [
    # v1/user/sms 发送短信的地址和个人主页的地址相似，但是这里用sms，即username不能是sms（视图函数会进错）
    # path('<str:username>',views.UserViews.as_view()),
    # path('<str:username>/avatar',views.users_views),
    # path('<str:username>/password',views.change_password),

    # 试用
    path('sms',views.sms_view),
    path('register/',views.register_show,name='register'),
    path('login/', views.login_show, name='login'),
    path('loginout/', views.loginout_view, name='loginout'),
]