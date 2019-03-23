from django.shortcuts import render
from django.http import request
from .models import Jobs

# Create your views here.
def home(request):
    job=Jobs.objects
    return render(request,'jobs/home.html',{"job":job})