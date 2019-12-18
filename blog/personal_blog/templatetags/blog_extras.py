from django import template

from personal_blog.models import Post, Category, Tag

register = template.Library()


@register.inclusion_tag('personal_blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):  # 最新文章模板标签
    return {
        'recent_post_list': Post.objects.all().order_by('-created_time')[:num]
    }


@register.inclusion_tag('personal_blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):  # 归档模板标签
    return {  # created_time: Post的创建时间, month: 精准度, order='DESC': 表明降序排列(离当前越近的时间排在前面)
        'date_list': Post.objects.dates('created_time', 'month', order='DESC'),  # Post.object.dates方法会返回一个列表
    }


@register.inclusion_tag('personal_blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):  # 分类模板标签
    return {
        'category_list': Category.objects.all(),
    }


@register.inclusion_tag('personal_blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }
