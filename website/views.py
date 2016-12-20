from django.core.files import File
from django.contrib.auth.decorators import login_required
from django.db import models
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import login
from django.template import Context, Template
from django.forms import *
from django.core.serializers.json import DjangoJSONEncoder
import json, re
from users.models import *
from website.models import Post
from urllib import request
import os

def index(request):
    template = loader.get_template('website/index.html')
    officers = UserProfile.objects.filter(user_type=3, approved=True)
    # context = RequestContext(request, { 'officers': officers })
    # return HttpResponse(template.render(context))
    posts = [Post() for i in range(5)]
    post_data = open("website/posts.out","r")
    post_data = json.loads( post_data.read() )
    img_path = 'static/website/images/icons/post'
    for i in range(len(posts)):
        posts[i].text = post_data[i][0]
        posts[i].url = post_data[i][1]
        posts[i].date = post_data[i][2]
        posts[i].img_video = img_path+str(i)+".jpg"
        posts[i].likes = post_data[i][5]
    context = {
    	'posts' : posts,
    	'officers': officers
    }
    template.render(Context(context))

    return render(request, 'website/index.html', context)

def oh(request):
    return render(request, 'website/oh.html', {})

def ir(request):
	return render(request, 'website/ir.html', {})
