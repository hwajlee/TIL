from django.urls import path
from . import views # form opencv_webapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'opencv_webapp'

urlpatterns = [
    path('', views.first_view, name='first_view'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
<<<<<<< Updated upstream
=======
    path('detect_face/', views.detect_face, name='detect_face'),
>>>>>>> Stashed changes
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
