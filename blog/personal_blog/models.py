import markdown
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags


class Category(models.Model):  # 类别
    name = models.CharField(max_length=100)  # 名称

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):  # 标签
    name = models.CharField(max_length=100)  # 名称

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):  # 文章
    title = models.CharField('标题', max_length=70)  # 文章标题
    body = models.TextField('正文')  # 文章正文
    created_time = models.DateTimeField('创建时间', default=timezone.now)  # 文章创建时间
    modified_time = models.DateTimeField('修改时间')  # 文章最后一次修改时间
    excerpt = models.CharField('摘要', max_length=200, blank=True)  # 文章摘要，可以为空
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)  # 文章分类
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)  # 文章标签
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)  # 文章作者

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):  # 保存模型实例数据到数据库的逻辑
        self.modified_time = timezone.now()
        md = markdown.Markdown(extensions=[  # 先实例化一个MD类，用于渲染body文本  由于摘要不需要生成文章目录，所以没有写
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        # 先将MD文本渲染HTML文本，strip_tags去掉HTML文本的全部HTML标签 再从文本中摘取前54个字符赋值excerpt
        self.excerpt = strip_tags(md.convert(self.body))[:54]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # 获取绝对路径  自定义
        return reverse('personal_blog:detail', kwargs={'pk': self.pk})
