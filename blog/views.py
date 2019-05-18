from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .models import Post

def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') (para verlo todo)
    #    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:2] (para ver solo los dos últimos)
    posts = Post.para_ver_los_dos_ultimos()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail (request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})



