# 序列化工具
# 1.在想要序列化数据的项目中导入该文件,views中导入该class
# 2.在接收序列化数据的views中导入该文件
# 3.fields中放入想要传输的字段
# 4.在setting的app中添加库
# 序列化时：
# xxx= 该文件的class名(result)
# xxx.data

# 序列化库
from rest_framework import serializers
from data.models import DataProfile
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataProfile
        fields = ('PH','TDS','TU','TEM')