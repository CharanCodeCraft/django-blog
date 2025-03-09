from django.shortcuts import render
from django.http import HttpResponse as httpResponse
from .models import Post 
from .forms import createBlog
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context={
        'posts': Post.objects.all(),
        'title': 'home'
    }
    return render(request, "blog/home.html", context)

def blogs(request):
    context={
        'posts': Post.objects.filter(author=request.user),
    }
    return render(request, "blog/blogs.html",context)

@login_required
def createblog(request):
    if request.POST:
        c_form=createBlog(request.POST)
        if c_form.is_valid(): 
            post = c_form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request,f'Your blog has been created')
            return redirect('blogs')
    else:
        c_form=createBlog()
    context={
        'c_form':c_form
    }
    return render(request, "blog/createblog.html",context)

def singleblog(request,pk):
    context={
        'post': Post.objects.get(pk=pk)
    }
    return render(request, "blog/singleblog.html",context)

@login_required
def deleteblog(request,pk):
    if request.user != Post.objects.get(pk=pk).author:
        messages.warning(request,f'You do not have permission to delete this blog')
        return redirect('blogs')
    else:
        Post.objects.get(pk=pk).delete()
    messages.success(request,f'Your blog has been deleted')
    return redirect('blogs')
@login_required
def editblog(request,pk):
    if request.user != Post.objects.get(pk=pk).author:
        messages.warning(request,f'You do not have permission to edit this blog')
        return redirect('blogs')
    else:
        if request.POST:
            c_form=createBlog(request.POST,instance=Post.objects.get(pk=pk))
            if c_form.is_valid(): 
                c_form.save()
                messages.success(request,f'Your blog has been updated')
                return redirect('blogs')
        else:
            c_form=createBlog(instance=Post.objects.get(pk=pk))
    context={
        'c_form':c_form
    }
    return render(request, "blog/editblog.html",context)