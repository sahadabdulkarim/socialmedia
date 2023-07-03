from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    bio = models.TextField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)


class Follow(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers"
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )
