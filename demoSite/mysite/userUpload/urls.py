from django.urls import path

from . import views

app_name = 'userUpload'
urlpatterns = [
	path('', views.index, name='index'),
    path('upload/', views.userUpload, name='upload'),
]