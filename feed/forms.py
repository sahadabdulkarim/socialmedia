from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    caption = forms.CharField(widget=forms.TextInput, max_length=100)
    description = forms.CharField(widget=forms.TextInput)
    image = forms.ImageField(widget=forms.ClearableFileInput)

    class Meta:
        model = Post
        fields = ["caption", "image_or_video"]
