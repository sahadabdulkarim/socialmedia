from django import forms
from .models import User
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name")
    Last_name = forms.CharField(label="Last Name")
    email = forms.EmailField(label="Email address")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "Last_name",
            "email",
            "password",
            "password2",
        ]

    def clean(self, *args, **kwargs):
        first_name = self.cleaned_data.get("first_name")
        Last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError("Passwords do not match")

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email has already been registered")

        return super(UserRegisterForm, self).clean(*args, **kwargs)
