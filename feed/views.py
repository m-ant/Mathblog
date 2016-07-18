from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
	return render(request, 'feed/index.html', {'posts' : posts})




def educational_activities(request):
	return render(request, 'educational_activities/educational_activities.html')

def gallery(request):
	return render(request, 'gallery/gallery.html')

def lessons(request):
	return render(request, 'lessons/lessons.html')

def zno(request):
	return render(request, 'zno/zno.html')