from django.shortcuts import render
from createaccount.forms import UserForm
from django.contrib.auth.models import User

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

def user(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			login = form.cleaned_data['Login']
			pwd1 = form.cleaned_data['Password']
			pwd2 = form.cleaned_data['Password_bis']
			email = form.cleaned_data['Email']
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
				envoi = True
	else:
		form = UserForm()
	return render(request, 'createaccount/createaccount.html', locals())
