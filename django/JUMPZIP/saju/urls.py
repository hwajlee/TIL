# saju URL
from django.urls import path 
from . import views 

# 변수명 반드시 app_name에 고정 
app_name = 'saju'

urlpatterns = [
    path('info/', views.info, name='info'),
    path('result/', views.result, name='result'),
]
