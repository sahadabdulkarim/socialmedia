from django.shortcuts import get_object_or_404, redirect, render
from feed.forms import PostForm

from feed.models import Post


def add_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}

    return render(request, "posts/create_post.html", context)


def edit_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm(instance=post)

    context = {"form": form, "post_id": post_id}
    return render(request, "posts/edit_post.html", context)


def delete(request, post_id):
    post = Post.objects.get(post_id=post_id)
    post.delete()
    return redirect("home")
