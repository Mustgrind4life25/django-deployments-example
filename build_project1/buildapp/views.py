from django.shortcuts import render
from buildapp.forms import UserForm,UserProfileInfoForm


# django login imports
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required 



# Create your views here.
def index(request):
	return render(request, 'buildapp/index.html')


def register(request):

	# this will see if someone is registered or not
	registered = False 


	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(data=request.POST)


		# check to see if the forms are valid

		if user_form.is_valid() and profile_form.is_valid():

			# Grab the user form save it and hash the password typed in by the user 
			user = user_form.save()
			user.set_password(user.password)# this is what hashes the password
			user.save() 

			# profile form check 
			profile= profile_form.save(commit=False)
			# sets up one to one relationship
			profile.user = user

			# this connects to the models profile_pic variable
			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()

			# if everything is true then do this
			registered = True
		else:
			print(user_form.errors,profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()

	return render(request,'buildapp/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
 

# login section. 

def user_login(request):

	# this checks if the user is logged on 
	if request.method == 'POST':
		username = request.POST.get('username')#username and password are being pulled from login html
		password = request.POST.get('password')
		


		#django authentication which checks if the user who just typed in this data is authenticated
		user = authenticate(username=username,password=password)

		# if logged user will be redirected to the home page
		if user:
			if user.is_active:
				login(request,user)#this logins the user
				return HttpResponseRedirect(reverse('index'))

			else:
				return HttpResponse("ACCOUNT NOT ACTIVE")

		else:
			print('Someone tired to login and failed!')
			print('Username: {} and password {}'.format(username,password))
			return	HttpResponse('invalid login details supplied!')

	else:
		return render(request,'buildapp/login.html',{})

	


@login_required
def special(request):
	return HttpResponse("You are logged in Nice!")


#this means that someone has to be logged in 
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))
