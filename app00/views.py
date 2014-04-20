from django.shortcuts import render

def index(request):
	return render(request, 'app00/index.html')
