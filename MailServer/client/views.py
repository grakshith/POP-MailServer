from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth import logout
# Create your views here.
from django.http import HttpResponse
app_name='client'
@login_required(login_url="login/")
def home(request):
	if(request.user.is_authenticated()):
		return render(request,'client/home.html')
	else:
		return redirect('login/')

def user_logout(request):
	logout(request)
	return redirect('/')
