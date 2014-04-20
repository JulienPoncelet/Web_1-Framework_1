from django import forms
from django.forms import PasswordInput

class LoginForm(forms.Form):
	Login = forms.CharField(max_length = 16, required = True)
	Password = forms.CharField(max_length = 16, required = True, widget = PasswordInput())
