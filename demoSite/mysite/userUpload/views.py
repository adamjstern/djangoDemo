from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def userUpload(request):
	return render(request, 'userUpload/userUpload.html')