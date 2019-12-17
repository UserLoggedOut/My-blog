from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # 配置子路由
]
