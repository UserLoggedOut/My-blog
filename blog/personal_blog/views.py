from django import http
from django.shortcuts import render
from django.views import View


class IndexView(View):  # 显示主页
    def get(self, request):
        return render(request, 'personal_blog/index.html', context={
            'title': '我的博客首页',
            'welcome': '欢迎访问我的博客首页'
        })
