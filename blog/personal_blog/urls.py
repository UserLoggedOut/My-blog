from django.urls import path

from . import views

app_name = 'personal_blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # 主页
    path('posts/<int:pk>/', views.DetailView.as_view(), name='detail'),  # 详情页
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archive'),  # 归档页
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'),  # 分类页
    path('tags/<int:pk>/', views.TagsView.as_view(), name='tags'),
]
