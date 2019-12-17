from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):  # 类别
    name = models.CharField(max_length=100)  # 名称


class Tag(models.Model):  # 标签
    name = models.CharField(max_length=100)  # 名称


class Post(models.Model):  # 文章
    title = models.CharField(max_length=70)  # 文章标题
    body = models.TextField()  # 文章正文
    created_time = models.DateTimeField()  # 文章创建时间
    modified_time = models.DateTimeField()  # 文章最后一次修改时间
    excerpt = models.CharField(max_length=200, blank=True)  # 文章摘要，可以为空
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # 文章分类
    tags = models.ManyToManyField(Tag, blank=True)  # 文章标签
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 文章作者
