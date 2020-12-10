from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.core.mail import send_mail


# Create your views here.

def index(request):
	posts = Post.objects.all()
	context = {
		'posts':posts
	}
	return render(request, 'blog/index.html', context)
