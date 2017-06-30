from django.shortcuts import render
from django.utils import timezone
from .models import Post #connect Post model to this view code
from django.shortcuts import render, get_object_or_404


# Create your views here.



def post_list(request): #take a request arguement

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts}) #renders the request on the html page


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})