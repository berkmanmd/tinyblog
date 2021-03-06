from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    subject = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
    user = models.ForeignKey(User)
    post_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.subject

class Comment(models.Model):
    comment = models.CharField(max_length=2000)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.comment

class User_Attr(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=10, blank=True)
    photo_url = models.CharField(max_length=200, blank=True)
