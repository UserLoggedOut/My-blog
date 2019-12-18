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
        post.toc = md.toc  #
        return render(request, 'personal_blog/detail.html', context={'post': post})
