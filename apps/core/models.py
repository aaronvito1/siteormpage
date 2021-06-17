from django.db import models

# Create your models here.

# Creating a blog post area where 'authenticated' users can post their ideas
class Post(models.Model):
	first_name = models.CharField(max_length=30, default='name')
	last_name = models.CharField(max_length=30, default='name')
	# name = models.CharField(max_length=30, default='SOME STRING')
	title = models.CharField(max_length=255)
	body = models.TextField()