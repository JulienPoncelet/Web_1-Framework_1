from django import forms

class UserForm(forms.Form):
	Login = forms.CharField(max_length = 16, required = True)
	Password = forms.CharField(max_length = 16, required = True)
	Password_bis = forms.CharField(max_length = 16, required = True)
	Email = forms.EmailField(required = True)
