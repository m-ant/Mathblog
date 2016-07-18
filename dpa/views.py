from django.shortcuts import render


def dpa(request):
	return render(request, 'dpa/dpa.html', {})
