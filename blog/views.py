from django.shortcuts import render,redirect
from blog.models import BlogModel
from blog.forms import BlogForm

def add_blog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = BlogForm()
    return render(request, 'blog/add_blog.html', {'form':form})

def blog(request):
    blogs = BlogModel.objects.order_by('-timestamp')
    return render(request, 'blog/blog.html', {'blogs': blogs})
