# Master URL
from django.contrib import admin
from django.urls import path, include # include => 넘기기용 함수 

urlpatterns = [
    path('admin/', admin.site.urls),
    # URL pattern이 'review'로 시작하면 => review/url.py 에게 넘겨졌다.
    path('review/', include('review.urls')), # review app 안에 urls.py
    path('data/', include('data.urls')),
]
