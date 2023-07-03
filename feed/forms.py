from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["caption", "image_or_video"]


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
