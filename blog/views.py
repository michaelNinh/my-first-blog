from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post #connect Post model to this view code
from django.shortcuts import render, get_object_or_404
from .forms import PostForm


# Create your views here.



def post_list(request): #take a request arguement

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts}) #renders the request on the html page


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):

    if request.method == "POST": #if the request method is equal to POST
        form = PostForm(request.POST) #form is defined as postform object with POST passed in
        if form.is_valid():
            post = form.save(commit=False) #save the form
            post.author = request.user #set author to user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk) #redirect page to post
    else:
        form = PostForm() #create form variable as a new PostForm

    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})