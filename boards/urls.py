from django.contrib import admin
from django.urls import path , include
from . import views

app_name='boards'

urlpatterns = [
    path('', views.index ),
    path('new/', views.new), #사용자 입력을 받아서 게시글을 작성하는 곳
    path('create/', views.create), # 사용자가 입력한 데이터를 전송받고 db에 저장
    path('<int:id>/', views.detail),
    path('<int:id>/delete/', views.delete),
    path('<int:id>/edit/', views.edit),
    path('<int:id>/update/', views.update),
]
