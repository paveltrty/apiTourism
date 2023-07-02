from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    Name = models.CharField(max_length=255)
    Location = models.TextField(blank=True)
    Tags = models.TextField(blank=True)
    rating = models.IntegerField(default=0)
    Description = models.TextField(blank=True)
    Price = models.IntegerField(default=0)
    Is_Approved = models.BooleanField(default=False)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    Description = models.TextField(blank=True)
    Post = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Account(models.Model):
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Is_Admin = models.BooleanField(default=False)


class Album(models.Model):
    Image = models.ImageField(upload_to='post_images/')
    Post = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
