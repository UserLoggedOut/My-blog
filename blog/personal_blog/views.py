import re

import markdown
from django.shortcuts import render, get_object_or_404
from django.views import View

from personal_blog.models import Post


class IndexView(View):  # 显示主页
    def get(self, request):
        post_list = Post.objects.all().order_by('-created_time')
        return render(request, 'personal_blog/index.html', context={'post_list': post_list})


class DetailView(View):  # 显示详情页
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        # 解析Markdown
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
        ])
        post.body = md.convert(post.body)
        m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>',
                      md.toc, re.S)  # 如果文章没有任何标题元素时，MD就提取不出目录结构，post.toc就是一个空的<div>标签
        post.toc = m.group(1) if m is not None else ''  # 使用三目运算符判断是否有数据
        return render(request, 'personal_blog/detail.html', context={'post': post})
