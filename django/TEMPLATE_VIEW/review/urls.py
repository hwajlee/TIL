# review/urls.py
from django.urls import path
from . import views

# 변수명 반드시 app_name 고정 
app_name = 'review'

#  url 구성 앞에 'review/'는 이미 master url에서 검사가 끝남
urlpatterns = [
    # 패턴 '(review/)index'가 요청으로 들어온다면, ?? 함수 실행 
    path('index/', views.index, name='index'),
    path('hello/', views.hello, name='hello'), 
]
