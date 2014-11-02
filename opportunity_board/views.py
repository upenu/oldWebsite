from django.shortcuts import render
from opportunity_board.models import *
from opportunity_board.forms import *
from datetime import datetime

# Create your views here.
def create_post(request):
	if request.method == 'POST':
		post_form = PostForm(request.POST)

		if post_form.is_valid():
			post = post_form.save()
		else:
			print(str(post_form.errors))
	else:
		post_form = PostForm()

	return render(request, "opportunity_board/create.html",
		{'post_form': post_form})

def delete_post(request, post_id):
	post = Post.objects.get(id=post_id)
	post.delete()
	return index(request)

def index(request):
	posts = Post.objects.all().order_by('date_published')[::-1]
	return render(request, "opportunity_board/index.html",
		{'posts': posts})

def display_post(request, post_id):
	post = Post.objects.get(id=post_id)
	return render(request, "opportunity_board/post.html",
		{'post': post})

