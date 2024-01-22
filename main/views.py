from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404


def post_list(request):
    posts = Post.objects.order_by('-date_created')
    return render(request, 'post_list.html', {'posts': posts})


def post_detail (request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})