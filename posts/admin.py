from django.contrib import admin
from posts.models import Post, PostReply

admin.site.register(Post)
admin.site.register(PostReply)