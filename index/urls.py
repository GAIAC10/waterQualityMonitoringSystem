from django.urls import path
from . import views

app_name='index'
urlpatterns = [
    path('historys/', views.History.as_view()),
    path('main/',views.newdata_show,name='index'),
    path('history/',views.history_show,name='history'),
    # 在iframe中镶嵌的地图
    path('baidu/',views.baiDu_api,name='baidu'),
    path('map/', views.map, name='map'),
    path('instrument/',views.instrument,name='instrument'),
    path('instrument_data/', views.instrument_data),
    path('chart/', views.chart_show,name='chart'),

]