from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=50,
				required=True,
				label="",
				widget=forms.TextInput({'class':'form-control mb-3'
					,'placeholder':'Email'}))
	username = forms.CharField(max_length=50,
				required=True,
				label="",
				widget=forms.TextInput({'class':'form-control mb-3'
					,'placeholder':'Username'}))
	password1 = forms.CharField(max_length=50,
				required=True,
				label="",
				widget=forms.TextInput({'class':'form-control mb-3','type':'password'
					,'placeholder':'Password'}))
	password2 = forms.CharField(max_length=50,
				required=True,
				label="",
				widget=forms.TextInput({'class':'form-control mb-3','type':'password'
					,'placeholder':'Password'}))
	class Meta:
		model = User
		fields = ['username', 'email']

class UserAuthenticationForm(AuthenticationForm):
	username = forms.EmailField(max_length=50,
				required=True,
				label="",
				widget=forms.TextInput({'class':'form-control mb-3'
					,'placeholder':'Email'}))
	password = forms.CharField(max_length=50,
				required=True,
				label="",
				widget=forms.TextInput({'class':'form-control mb-3','type':'password'
					,'placeholder':'Password'}))