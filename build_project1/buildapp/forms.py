from django import forms
from django.contrib.auth.models import User
from buildapp.models import UserProfileInfo

# this creates the email and password fields for register form
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	# this is what is being asked to be returned in the registration page
	class Meta():
		model = User
		fields = ('username', 'email','password')

	# this to is being returned to the registration page
class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('portfolio_site', 'profile_pic')