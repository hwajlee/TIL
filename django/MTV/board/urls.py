# board urls.py
from django.urls import path 
from . import views 

app_name = 'board'

urlpatterns = [
    # 글쓰기: board/form/
    path('form/', views.form, name='form'),
    # 글 저장: board/create
    path('create/', views.create, name='create'),

    # 글 목록: board/
    path('', views.main, name='main'),
    # board/1 
    path('<int:posting_pk>/', views.content, name='content'),

    # board/1/correct
    path('<int:posting_pk>/correct/', views.correct, name='correct'),
    # board/1/update
    path('<int:posting_pk>/update', views.update, name='update'),

    # board/1/delete
    path('<int:posting_pk/delete', views.delete, name='delete'),
]
