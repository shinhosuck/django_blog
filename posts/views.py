from django.shortcuts import render


def home(request):

    context = {
        'data': 'hell world'
    }

    return render(request, 'posts/home.html', context)
