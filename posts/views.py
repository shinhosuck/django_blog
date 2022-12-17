from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, PostReply
from posts.forms import PostReplyForm


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
    

def post_reply(request, pk):
    user = request.user
    replied_to = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostReplyForm(request.POST)
        if form.is_valid():
            data = form.save()
            reply = PostReply.objects.get(pk=data.pk)
            reply.user = user
            reply.post = replied_to
            reply.save()
        return redirect('posts:home')
    else:
        form = PostReplyForm()
        context = {
            'form': form
        }
        return render(request, 'posts/post_reply.html', context)