from django.db import models
import random

# 随机的签名
def default_sign():
    signs=['每一个不曾起舞的日子,都是对生命的辜负.','给我们赦免的,是忏悔而不是牧师.','一旦被贴上标签,你就很难逃脱.','才貌出众的人多半在劫难逃.']
    return random.choice(signs)

# Create your models here.
class UserProfile(models.Model):
    # 在model中有primary_key=True属性的字段时，则model不会送id字段
    username=models.CharField(max_length=11,verbose_name='用户名',primary_key=True)
    password=models.CharField(max_length=32)
    phone=models.CharField(max_length=11)
    # models.ImageField(头像)和models.FileField（文件）相似（前者继承于后者）
    avatar=models.ImageField(upload_to='avatar',null=True)
    sign=models.CharField(max_length=50,verbose_name='个人签名',default=default_sign)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

    class Meta:
       db_table='users_info'