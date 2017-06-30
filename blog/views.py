from django.shortcuts import render

# Create your views here.



def post_list(request): #take a request arguement
    return render(request, 'blog/post_list.html', {}) #call render