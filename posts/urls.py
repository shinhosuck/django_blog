from django.urls import path
from posts.views import home


app_name = 'posts'

urlpatterns = [
    path('', home, name='home')
]
