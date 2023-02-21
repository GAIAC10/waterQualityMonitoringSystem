from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from data.models import DataProfile
from django.views import View
from index.serializable import DataSerializer

# Create your views here.
def newdata_show(request):
    datas=DataProfile.objects.order_by('-id').first()
    id=datas.id
    PH=datas.PH
    TDS=datas.TDS
    TU=datas.TU
    TEM=datas.TEM
    TIME=datas.created_time
    context={'id':id,'PH':PH,'TDS':TDS,'TU':TU,'TEM':TEM,'TIME':TIME}
    return render(request,'index/index.html',context=context)


class History(View):
    def get(self,request):
        # DataProfile.objects.order_by('-id').first()-->DataProfile(模型) 前端ajax获取不到该数据 mvc
        # DataProfile.objects.last() 是将一个obj数据反过来，取第一个数据

        data1 = DataProfile.objects.last()
        id1 = data1.id
        data2=DataProfile.objects.get(id=id1-1)
        id2=data2.id
        data3=DataProfile.objects.get(id=id2-1)
        id3=data3.id
        data4=DataProfile.objects.get(id=id3-1)
        id4=data4.id
        data5=DataProfile.objects.get(id=id4-1)
        id5=data5.id
        data6=DataProfile.objects.get(id=id5-1)
        id6=data6.id
        data7=DataProfile.objects.get(id=id6-1)
        id7=data7.id
        data8=DataProfile.objects.get(id=id7-1)

        # 获取全套数据
        data1_PH=data1.PH
        data1_TU=data1.TU
        data1_TDS=data1.TDS
        data1_TEM=data1.TEM

        data2_PH=data2.PH
        data2_TU=data2.TU
        data2_TDS=data2.TDS
        data2_TEM=data2.TEM

        data3_PH=data3.PH
        data3_TU=data3.TU
        data3_TDS=data3.TDS
        data3_TEM=data3.TEM

        data4_PH=data4.PH
        data4_TU=data4.TU
        data4_TDS=data4.TDS
        data4_TEM=data4.TEM

        data5_PH=data5.PH
        data5_TU=data5.TU
        data5_TDS=data5.TDS
        data5_TEM=data5.TEM

        data6_PH=data6.PH
        data6_TU=data6.TU
        data6_TDS=data6.TDS
        data6_TEM=data6.TEM

        data7_PH=data7.PH
        data7_TU=data7.TU
        data7_TDS=data7.TDS
        data7_TEM=data7.TEM

        data8_PH=data8.PH
        data8_TU=data8.TU
        data8_TDS=data8.TDS
        data8_TEM=data8.TEM

        result = {'code': 200,
        'data': {
        "data1ph":float(data1_PH),
        "data1tu":float(data1_TU),
        "data1tds":float(data1_TDS),
        "data1tem":float(data1_TEM),

        "data2ph":float(data2_PH),
        "data2tu":float(data2_TU),
        "data2tds":float(data2_TDS),
        "data2tem":float(data2_TEM),

        "data3ph":float(data3_PH),
        "data3tu":float(data3_TU),
        "data3tds":float(data3_TDS),
        "data3tem":float(data3_TEM),

        "data4ph":float(data4_PH),
        "data4tu":float(data4_TU),
        "data4tds":float(data4_TDS),
        "data4tem":float(data4_TEM),

        "data5ph":float(data5_PH),
        "data5tu":float(data5_TU),
        "data5tds":float(data5_TDS),
        "data5tem":float(data5_TEM),

        "data6ph":float(data6_PH),
        "data6tu":float(data6_TU),
        "data6tds":float(data6_TDS),
        "data6tem":float(data6_TEM),

        "data7ph":float(data7_PH),
        "data7tu":float(data7_TU),
        "data7tds":float(data7_TDS),
        "data7tem":float(data7_TEM),

        "data8ph":float(data8_PH),
        "data8tu":float(data8_TU),
        "data8tds":float(data8_TDS),
        "data8tem":float(data8_TEM),
        }}

        return JsonResponse(result)


def history_show(request):
    # 最新的数据是data1
    data1=DataProfile.objects.order_by('-id').first()
    id1=data1.id
    print("id1是%s"%(id1))
    data2=DataProfile.objects.get(id=id1-1)
    id2=data2.id
    data3=DataProfile.objects.get(id=id2-1)
    id3=data3.id
    data4=DataProfile.objects.get(id=id3-1)
    id4=data4.id
    data5=DataProfile.objects.get(id=id4-1)
    id5=data5.id
    data6=DataProfile.objects.get(id=id5-1)
    id6=data6.id
    data7=DataProfile.objects.get(id=id6-1)
    id7=data7.id
    data8=DataProfile.objects.get(id=id7-1)
    id8=data8.id
    data9=DataProfile.objects.get(id=id8-1)
    id9=data9.id
    data10=DataProfile.objects.get(id=id9-1)
    id10=data10.id
    data11=DataProfile.objects.get(id=id10-1)
    id11=data11.id
    data12=DataProfile.objects.get(id=id11-1)
    id12=data12.id
    data13=DataProfile.objects.get(id=id12-1)
    id13=data13.id

    # PH=data1.PH
    # TDS=data1.TDS
    # TU=data1.TU
    # TEM=data1.TEM
    # TIME=data1.created_time
    # context={'id':id,'PH':PH,'TDS':TDS,'TU':TU,'TEM':TEM,'TIME':TIME}

    context={
        'data1':data1,
        'data2':data2,
        'data3': data3,
        'data4': data4,
        'data5': data5,
        'data6': data6,
        'data7': data7,
        'data8': data8,
        'data9': data9,
        'data10': data10,
        'data11': data11,
        'data12': data12,
    }
    return render(request,'index/history.html',context=context)


def baiDu_api(request):
    return render(request, 'index/baiDu_api.html')

def map(request):
    return render(request, 'index/map1.html')

def instrument(request):
    return render(request,'index/instrument.html')

def instrument_data(request):
    datas=DataProfile.objects.order_by('-id').first()
    PH=datas.PH
    TDS=datas.TDS
    TU=datas.TU
    TEM=datas.TEM
    # context={'PH':PH,'TDS':TDS,'TU':TU,'TEM':TEM}
    # return render(request,'index/instrument.html',context=context)
    result = {'code': 200,
              'data': {
                  "ph": PH,
                  "tu": TU,
                  "tds": TDS,
                  "tem": TEM
              }}
    return JsonResponse(result)

def chart_show(request):
    return render(request, 'index/chart.html')
