from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.core.files.storage import FileSystemStorage

from .forms import VisitorForm
from .models import Visitor

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

def visitorList(request):
	visitors = Visitor.objects.all()
	return render(request, 'userUpload/visitorList.html', {
		'visitors': visitors
	})

def visitorUpload(request):
	if request.method == 'POST':
		form = VisitorForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('visitorList')
	else:
		form = VisitorForm()
	return render(request, 'userUpload/visitorUpload.html', {
		'form': form
	})


