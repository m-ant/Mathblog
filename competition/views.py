from django.shortcuts import render


def competition(request):
	return render(request, 'competition/competition.html', {})