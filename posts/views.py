from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post



def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/home.html', context)

def post_detail(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)
        context = {
            'post': post
        }
        return render(request, 'posts/post_detail.html', context)
    except:
        return redirect('posts:home')
    