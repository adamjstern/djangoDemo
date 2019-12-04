from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the upload index.")

def userUpload(request):
	context = {}
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		print(uploaded_file.name)
		print(uploaded_file.size)
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		context['url'] = fs.url(name)
	return render(request, 'userUpload/userUpload.html', context)