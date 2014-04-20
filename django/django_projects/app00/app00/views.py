from django.shortcuts import render

def index(request):
	auth = False
	if request.user.is_authenticated():
		group = request.user.groups.values_list('name',flat=True)[0]
		login = request.user.username.title
		auth = True
	return render(request, 'app00/index.html', locals())
