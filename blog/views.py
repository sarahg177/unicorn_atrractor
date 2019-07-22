from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm


def get_posts(request):
    """Create a view that will return a list of posts that were published prior to 'now' and render them
    to 'blogposts.html' template"""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogpost.html", {'posts': posts})


def create_or_edit(request):
    """Create a view that allows user to create or edit a post"""
    post = Post.objects.get(id=request.GET.get('id'))
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(get_posts)
