import requests
from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from django.db import models
from .models import Post

# class PostBlog(forms.Form):
class PostForm(forms.Form):
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	title= forms.CharField()
	body = forms.CharField(widget=forms.Textarea)
	created= models.DateTimeField(auto_now_add=True)

def index(request):
	# content_html = open("apps/core/templates/index.html").read()
	print('Index page being visited')
	context = {
		# "content": content_html, 
	}
	return render(request, "index.html", context)

def about(request):
	# content_html = open("apps/core/templates/about.html").read()
	print('About page being visited')
	context = {
		# "content": content_html, 
	}
	return render(request, "about.html", context)

def portfolio(request):
	# content_html = open("apps/core/templates/portfolio.html").read()
	print('Portfolio page being visited')
	response = requests.get('https://api.github.com/users/aaronvito1/repos')
	repos = response.json()
	context = {
		# "content": content_html,
		'github_repos': repos, 
	}
	return render(request, "portfolio.html", context)

def extra(request):
	# content_html = open("apps/core/templates/extra.html").read()
	print('Extra page being visited')
	context = {
		# "content": content_html, 
	}
	return render(request, "extra.html", context)

def blog(request):
	print('Blog page being visited')
	# content_html = open("apps/core/templates/blog.html").read()
	# CREATE POSTS
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			Post.objects.create(
				title=form.cleaned_data['title'],
				body=form.cleaned_data['body'],
				first_name=form.cleaned_data['first_name'],
				last_name=form.cleaned_data['last_name'],
				)
			return redirect('/')
	else:
		form=PostForm()

	blog_posts = Post.objects.all()
	context = {
		# "content": content_html, 
		"all_posts": blog_posts,
		"form": form,
	}
	return render(request, "blog.html", context)

def contact(request):
	# content_html = open("apps/core/templates/contact.html").read()
	print('Contact page being visited')
	context = {
		# "content": content_html, 
	}
	return render(request, "contact.html", context)

# def github_api(request):

#     return render(request, 'github.html', context)