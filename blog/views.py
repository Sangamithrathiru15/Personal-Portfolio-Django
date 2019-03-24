from django.shortcuts import render,get_object_or_404
from django.http import request
from .models import Blogs
# Create your views here.
def showblog(request):
    blog=Blogs.objects
    return render(request,"blog/blog.html",{"blog":blog})

def detail(request,blog_id):
    detailblog=get_object_or_404(Blogs,pk=blog_id)
    return render(request,"blog/detail.html",{"detail":detailblog})

