from django import http
from django.shortcuts import render
from django.views import View

from personal_blog.models import Post


class IndexView(View):  # 显示主页
    def get(self, request):
        post_list = Post.objects.all().order_by('-created_time')
        return render(request, 'personal_blog/index.html', context={'post_list': post_list})
