from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post, Like
from django.contrib.auth.decorators import login_required


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("post_detail", post_id=post.id)
    else:
        form = PostForm()
    return render(request, "posts/create_post.html", {"form": form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "posts/post_detail.html", {"post": post})


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect("post_detail", post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, "posts/edit_post.html", {"form": form, "post": post})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return render(request, "posts/delete_post.html", {"post": post})


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if Like.objects.filter(user=user, post=post).exists():
        like = Like.objects.get(user=user, post=post)
        like.delete()
    else:
        Like.objects.create(user=user, post=post)

    return redirect("post_detail", post_id=post.id)
