from django.contrib import admin

# Register your models here.
from personal_blog.models import Post, Category, Tag

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
