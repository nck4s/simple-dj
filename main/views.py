from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('-date_created')[:5]
    return render(request, 'post_list.html', {'posts': posts})


