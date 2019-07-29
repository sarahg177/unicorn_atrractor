from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post
from .forms import BlogPostForm


def get_posts(request):
    """Create a view that will return a list of posts that were published prior to 'now' and render them
    to 'blogposts.html' template"""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(posts, 5)  # Shows 5 blog posts per page

    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, "blogpost.html", {'blogs': blogs})


def create_post(request):
    """Create a view that allows user to create a post"""
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, "blogpostform.html", {'form': form})


def edit_a_blog(request):
    """Edit a blog post"""
    blog = Post.objects.get(id=request.GET.get('id'))
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm(instance=blog)
    return render(request, "blogpostform.html", {'form': form})


def delete_blog(request):
    """Delete a blog post"""
    post = Post.objects.get(id=request.GET.get('id'))
    post.delete()
    return redirect('blog_list')
