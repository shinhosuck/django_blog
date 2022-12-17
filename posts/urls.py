from django.urls import path
from posts.views import (
        home,
        post_detail,
        post_reply
    )


app_name = 'posts'

urlpatterns = [
    path('', home, name='home'),
    path('post/detail/<int:pk>', post_detail, name='post-detail'),
    path('post/reply/<int:pk>', post_reply, name='post-reply')
]
