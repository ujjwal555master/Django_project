# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from django.shortcuts import render

# List all posts
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'open_up/post_list.html', {'posts': posts})


# View a single post
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'open_up/post_detail.html', {'post': post})


# Create a new post
@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content, author=request.user)
        return redirect('post_list')
    return render(request, 'open_up/create_post.html')

# Edit a post
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('post_list')  # Prevent editing by non-authors

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_detail', post_id=post.id)
    return render(request, 'open_up/edit_post.html', {'post': post})

# Delete a post
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author:
        post.delete()
    return redirect('post_list')
