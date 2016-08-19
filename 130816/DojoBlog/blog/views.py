from django.shortcuts import render
from django.utils import timezone
from .models import Post

def showPosts(request):
    posts = Post.objects.filter(creation_date__lte=timezone.now()).order_by('creation_date')
    return render(request, 'blog/posts.html', {'posts':posts})


# Create your views here.
