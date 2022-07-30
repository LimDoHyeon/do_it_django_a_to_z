#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

#FBV
"""
def index(request):
    posts = Post.objects.all()

    return render(
        request,
        'blog/post_list.html',
        {
            'posts': posts,
        }
    )
"""

#CBV
class PostList(ListView):
    model = Post
    ordering = '-pk'
    #template_name = 'blog/post_list.html'

class PostDetail(DetailView):
    model = Post