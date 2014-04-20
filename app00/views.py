from django.shortcuts import render

def index(request):
	auth = False
	if request.user.is_authenticated():
		test = request.user.username.title
		auth = True
	return render(request, 'app00/index.html', locals())
