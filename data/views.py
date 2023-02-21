from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import DataProfile
from index.serializable import DataSerializer

def html_show(request):
    TDS=request.GET.get('TDS')
    PH=request.GET.get('PH')
    TU=request.GET.get('TU')
    TEM=request.GET.get('TEM')

    LON=request.GET.get('LON')
    LAT=request.GET.get('LAT')

    # <QueryDict: {'TDS': ['24.69'], 'PH': ['4.61'], 'TU': ['768.75']}>
    # data.objects.create(TDS=TDS,PH=PH,TU=int(float(TU)))
    DataProfile.objects.create(TDS=TDS,PH=PH,TU=TU,TEM=TEM,LON=LON,LAT=LAT)

    # 之后可以重新规划一个界面
    return render(request,'users/tang.html')