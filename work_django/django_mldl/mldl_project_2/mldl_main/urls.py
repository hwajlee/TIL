from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'mldl_main'

urlpatterns = [
    path('', views.index, name='index'),

    path('ml_iris/', views.ml_iris, name='ml_iris'),
    path('ml_iris/predict/', views.predict_iris, name='predict_iris'),

    path('dl_mnist/', views.dl_mnist, name='dl_mnist'),
    path('dl_mnist/predict/', views.predict_mnist, name='predict_mnist'),
    path('dl_mnist/delete/<str:file_name>/', views.delete_mnist, name='delete_mnist'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# 변수를 받아내서 처리하는 예시
# @ browser
# www.shopshop.com/product_detail/32/

# @ urls.py
# path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),

# @ views.py
# def product_detail(request, product_id):
#     selected_item = ProductTable.objects.filter(id=product_id)
