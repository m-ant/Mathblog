from django.shortcuts import render

# Create your views here.
def educational_activities(request):
	return render(request, 'educational_activities/educational_activities.html', {})
