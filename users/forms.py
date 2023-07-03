from django import forms
from .models import User, Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password", "profile_picture"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["date_of_birth", "gender", "bio", "website", "location"]
