from django.shortcuts import render, redirect
from .forms import postForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post


def postPage(request):
    if request.method == 'POST':
        form = postForm(request.POST)
        title = request.POST.get('title')
        body = request.POST.get('body')
        author = User.objects.filter(username=request.user.username).first()
        post = Post(title=title, body=body, author=author)
        post.save()
        return redirect(f'/post/{post.id}')
    else:
        form = postForm()
    return render(request, 'app/post.html', {'form': form})


@login_required(login_url='login')
def homePage(request):
    posts = Post.objects.all()
    return render(request, 'app/home.html', {'posts': posts})


def postUpdate(request, pk):
    if request.method == 'POST':
        user = User.objects.filter(username=request.user.username).first()
        post = Post.objects.get(id=pk, author=user)
        form = postForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
    else:
        form = postForm()
    return render(request, 'app/update-post.html', {'form': form, 'Post': post})
