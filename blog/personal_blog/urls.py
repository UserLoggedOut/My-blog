from django.urls import path

from . import views

app_name = 'personal_blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # 主页
    path('posts/<int:pk>', views.DetailView.as_view(), name='detail')  # 详情页
]
