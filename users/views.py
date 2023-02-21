from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse, HttpResponseRedirect
from django.core.cache import cache
from .models import UserProfile
import hashlib
import random
from django.conf import settings
from tools.sms import YunTongXin

# Create your views here.

class UserViews(View):
    # 注册 post
    # 注册所有的信息都传到该函数了
    def post(self,request):
        # 前端发送数据的类型是contentType:'application/json',如果用request.POST则取不到数据

        # 想要取到json数据:request.body
        json_str=request.body
        json_obj=json.loads(json_str)
        username=json_obj['username']
        password_1=json_obj['password_1']
        password_2=json_obj['password_2']
        phone=json_obj['phone']
        sms_num=json_obj['sms_num']

        # 参数基本检查

        # 两次密码是否正确
        if password_1!=password_2:
            result={'code':'10100','error':'两次输入的密码不同'}
            return JsonResponse(result)

        # 验证码比对
        old_code=cache.get('sms_%s'%(phone))
        if not old_code:
            result={'code':'10110','error':'验证码错误'}
            return JsonResponse(result)
        if int(sms_num)!=old_code:
            result={'code':'10111','error':'验证码错误'}
            return JsonResponse(result)

        # 用户名是否可用
        # get返回的是value(需要try一下)，filter返回的是编号（Q...set）（不用try）
        old_users=UserProfile.objects.filter(username=username)
        if old_users:
            result={'code':10101,'error':'该用户名已存在'}
            return JsonResponse(result)

        # 正确时
        # 向UserProfile插入数据（密码md5存储）
        p_m=hashlib.md5()
        # 将字符串转化为字节串
        p_m.update(password_1.encode())
        UserProfile.objects.create(username=username,password=p_m.hexdigest(),phone=phone)
        result={'code':200,'username':username,'data':{}}
        return JsonResponse(result)

# 用户注册
def register_show(request):
    return render(request, 'users/register.html')

# 用户登录
def login_show(request):
    return render(request, 'users/login.html')

# 发送短信（接受到电话号码 post）
def sms_view(request):
    if request.method!='POST':
        result={'code':10108,'error':'请使用POST表单提交'}
        return JsonResponse(result)
    json_str=request.body
    json_obj=json.loads(json_str)
    phone=json_obj['phone']
    # 生成随机码
    code=random.randint(1000,9999)
    print('phone',phone,'code',code)
    # 存储随机码（之前是redis，现在是django_redis（将redis和django的缓存结合））
    cache_key='sms_%s'%(phone)
    # 检查是否已经有发送的且没有过期的验证码
    old_code=cache.get(cache_key)
    if old_code:
        result={'code':10111,'error':'该验证码已经存在'}
        return JsonResponse(result)

    cache.set(cache_key,code,60)
    # 发送随机码->短信
    send_sms(phone,code)
    return JsonResponse({'code':200})

# 短信发送
def send_sms(phone,code):
    config={
        'accountSid':settings.ACCOUNTSID,
        'accountToken':settings.ACCOUNTTOKEN,
        'appId':settings.APPID,
        'templateId':settings.TEMPLATEID
    }
    yun=YunTongXin(**config)
    res=yun.run(phone,code)
    return res

# 退出登陆
def loginout_view(request):
    # session的删除
    # 1和2都是自己写的
    # 1.if 'username'  in request.session or 'uid' in request.session:
    # 2.if request.session.get('username') and request.session.get('uid'):
        # del request.session['username']
        # del request.session['uid']
    # cookie的删除
    # if 'remember' in request.POST:
        # if request.COOKIES.get('username') and request.COOKIES.get('uid'):
            # req_web=HttpResponseRedirect('/user/login')
            # req_web.delete_cookie('username')
            # req_web.delete_cookie('uid')
        # return HttpResponseRedirect('/user/login')
    # 删除session值：
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del  request.session['uid']
    # 删除Cookie：
    resp=HttpResponseRedirect('/index')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return render(request,'users/login.html')
