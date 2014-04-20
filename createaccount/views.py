from django.shortcuts import render
from createaccount.forms import UserForm
from django.contrib.auth.models import User

def user(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			login = form.cleaned_data['Login']
			pwd1 = form.cleaned_data['Password']
			pwd2 = form.cleaned_data['Password_bis']
			email = form.cleaned_data['Email']
			user = User.objects.create_user(login, email)
			user.set_password(pwd1)
			user.save()
			envoi = True
	else:
		form = UserForm()
	return render(request, 'createaccount/createaccount.html', locals())
