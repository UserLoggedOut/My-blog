from django.urls import path

from . import views

app_name = 'personal_blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # 主页
    path('posts/<int:pk>/', views.DetailView.as_view(), name='detail'),  # 详情页
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archive'),  # 归档页
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'),  # 分类页
    path('tags/<int:pk>/', views.TagsView.as_view(), name='tags'),
    path('full-width/', views.BlogView.as_view(), name='full-width'),  # 博客
    path('about/', views.AboutView.as_view(), name='about'),  # 关于
    path('contact/', views.ContactView.as_view(), name='contact'),  # 联系
    path(r'^search/$', views.SearchView.as_view(), name='search'),  # 全文搜索
]
