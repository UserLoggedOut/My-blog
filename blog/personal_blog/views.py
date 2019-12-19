import re

import markdown
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.views import View
from markdown.extensions.toc import TocExtension

from personal_blog.models import Post, Category, Tag


class IndexView(View):  # 显示主页
    def get(self, request):
        post_list = Post.objects.all().order_by('-created_time')

        paginator = Paginator(post_list, 5)
        page = request.GET.get('page', 1)
        current_page = page
        if paginator.num_pages > 11:
            if current_page-5 < 1:
                page_range = range(1, 11)
            elif current_page+5 > paginator.num_pages:
                page_range = range(current_page-5, paginator.num_pages+1)
            else:
                page_range = range(current_page-5, current_page+6)
        else:
            page_range = paginator.page_range
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)

        return render(request, 'personal_blog/index.html', locals())


class DetailView(View):  # 显示详情页
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.increase_reading()  # 阅读量+1
        # 解析Markdown
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            # 'markdown.extensions.toc'
            TocExtension(slugify=slugify)  # MD内置方法不能出路中文，所以我们使用Django自带的
        ])
        post.body = md.convert(post.body)
        m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>',
                      md.toc, re.S)  # 如果文章没有任何标题元素时，MD就提取不出目录结构，post.toc就是一个空的<div>标签
        post.toc = m.group(1) if m is not None else ''  # 使用三目运算符判断是否有数据
        return render(request, 'personal_blog/detail.html', context={'post': post})


class ArchiveView(View):  # 归档页面
    def get(self, request, year, month):
        # 这里使用了模型管理器(objects)的filter方法来过滤文章
        post_list = Post.objects.filter(created_time__year=year,  # 按照日期归档，所以根据文章发表的年和月来过滤
                                        created_time__month=month
                                        ).order_by('-created_time')
        return render(request, 'personal_blog/index.html', context={'post_list': post_list})


class CategoryView(View):  # 分类页面
    def get(self, request, pk):
        cate = get_object_or_404(Category, pk=pk)
        post_list = Post.objects.filter(category=cate).order_by('-created_time')
        return render(request, 'personal_blog/index.html', context={'post_list': post_list})


class TagsView(View):  # 标签页面
    def get(self, request, pk):
        t = get_object_or_404(Tag, pk=pk)
        post_list = Post.objects.filter(tags=t).order_by('-created_time')
        return render(request, 'personal_blog/index.html', context={'post_list': post_list})


class BlogView(View):  # 博客页面
    def get(self, request):
        return render(request, 'personal_blog/full-width.html')


class AboutView(View):  # 关于
    def get(self, request):
        return render(request, 'personal_blog/about.html')


class ContactView(View):  # 联系
    def get(self, request):
        return render(request, 'personal_blog/contact.html')
