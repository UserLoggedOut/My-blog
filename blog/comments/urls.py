from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.CommentView.as_view(), name='comment'),
]
