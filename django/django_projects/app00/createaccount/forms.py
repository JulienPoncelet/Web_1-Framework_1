from django import forms
from django.forms import PasswordInput

class UserForm(forms.Form):
	Login = forms.CharField(max_length = 16, required = True)
	Password = forms.CharField(max_length = 16, required = True, widget = PasswordInput())
	Password_bis = forms.CharField(max_length = 16, required = True, widget = PasswordInput())
	Email = forms.EmailField(required = True)
