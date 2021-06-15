from django.db import models

# Create your models here.

# Creating a blog post area where 'authenticated' users can post their ideas
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()