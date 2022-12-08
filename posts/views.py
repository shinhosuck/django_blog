from django.shortcuts import render
from posts.models import Post

def home(request):
    posts = Post.objects.all()
    # print(posts)
    context = {
        'posts': posts
    }
    return render(request, 'posts/home.html', context)
