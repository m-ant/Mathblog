from django.shortcuts import render

def zno(request):
	return render(request, 'zno/zno.html', {})
