from django.shortcuts import render
from django.contrib.auth.models import User, Group
from better.forms import UserForm

def user_exist(username):
	if User.objects.filter(username=username).count():
		return True
	return False

def email_exist(email):
	if User.objects.filter(email=email).count():
		return True
	return False

def pwd_same(pwd1, pwd2):
	if pwd1 == pwd2:
		return True
	return False

def add_user(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			login = form.cleaned_data['Login']
			pwd1 = form.cleaned_data['Password']
			pwd2 = form.cleaned_data['Password_bis']
			email = form.cleaned_data['Email']
			group = form.cleaned_data['Group']
			if not pwd_same(pwd1, pwd2):
				pwdFail = True
			elif user_exist(login):
				userExist = True
			elif email_exist(email):
				emailExist = True
			else:
				user = User.objects.create_user(login, email)
				user.set_password(pwd1)
				user.save()
				g = Group.objects.get(name=group)
				g.user_set.add(user)
				envoi = True
	else:
		form = UserForm()
	return render(request, 'better/createaccount.html', locals())

def go_test(request):
	if request.user.is_authenticated():
		group = request.user.groups.values_list('name', flat = True)[0]
		if group == "better_user":
			return True
	return False

def better(request):
	test = False
	test = go_test(request)
	return render(request, 'better/better.html', locals())
