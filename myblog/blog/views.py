# -*- coding: utf-8 -*-
from __future__ import unicode_literals

<<<<<<< HEAD
#from django.shortcuts import render
#from blog.models import BlogsPost
#from django.shortcuts import render_to_response
from .models import *
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    blog_list = BlogsPost.objects.all()
    template = loader.get_template('index.html')
    context = {
        'blog_list':blog_list
    }
    return HttpResponse(template.render(context, request))
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> origin/master
