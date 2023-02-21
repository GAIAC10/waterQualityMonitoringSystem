from django.db import models

# Create your models here.
class DataProfile(models.Model):
    id=models.AutoField('编号',primary_key=True)

    TDS=models.CharField('固体溶解度',max_length=50,default=None,null=True)
    PH=models.CharField('酸碱度',max_length=50,default=None,null=True)
    TU=models.CharField('浊度',max_length=50,default=None,null=True)
    TEM=models.CharField('温度',max_length=50,default=None,null=True)

    LON=models.CharField('经度',max_length=50,default=None,null=True)
    LAT=models.CharField('纬度',max_length=50,default=None,null=True)

    created_time=models.DateTimeField('创建时间',auto_now_add=True)

    class Meta:
       db_table='data_info'