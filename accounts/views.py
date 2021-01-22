from django.shortcuts import render

from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@method_decorator(csrf_exempt)
def logout_view(request):
	logout(request)
	return JsonResponse({'Result' : 'You are logged out now'})


@method_decorator(csrf_exempt)
def register_view(request):
	if request.user.is_authenticated:
		return JsonResponse({'Result' : " You are already logged in "})

	if request.method == 'POST':
		first_name = request.POST['d1']
		last_name = request.POST['d2']
		username = request.POST['d3']
		password = request.POST['d4']
		email = request.POST['d5']

		user = User.objects.create_user(
			username = username, password= password, email= email, 
			first_name= first_name, last_name= last_name)
		user.save()
		return JsonResponse({'Result' : 'User created'})


@method_decorator(csrf_exempt)
def login_view(request):
	if request.user.is_authenticated:
		return JsonResponse({'Result' : " You are already logged in "})

	if request.method == 'POST':
		name = request.POST.get('d3')
		password = request.POST.get('d4')

		user = authenticate(request, username= name, password= password)
		print(user)
		if user is not None:
			login(request, user)
			return JsonResponse({'Result' : " You are Logged in now "})
		else:
			return JsonResponse({'Result' : " Your credentials are wrong "})