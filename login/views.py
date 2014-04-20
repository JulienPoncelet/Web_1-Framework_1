from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from login.forms import LoginForm
from createaccount.views import user_exist

def match(request, username, pwd):
	user = authenticate(username=username, password=pwd)
	if user is not None:
		login(request, user)
		return True
	return False

def login_user(request):
	logged = False
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			login = form.cleaned_data['Login']
			pwd = form.cleaned_data['Password']
			if not user_exist(login):
				login = login
			elif not match(request, login, pwd):
				login = login
			else:
				logged = True
	else:
		form = LoginForm()
	return render(request, 'login/login.html', locals())
