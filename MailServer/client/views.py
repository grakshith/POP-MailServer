from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth import logout
# Create your views here.
from django.http import HttpResponse
from .forms import ComposeForm
import cli
app_name='client'
@login_required(login_url="login/")
def home(request):
	if(request.user.is_authenticated()):

		return render(request,'client/home.html')
	else:
		return redirect('login/')

def compose(request):
	if(request.method=='GET'):
		form=ComposeForm()
		return render(request,'client/compose.html',{'form':form})
	elif(request.method=='POST'):
		form=ComposeForm(request.POST)
		if form.is_valid():
			to=form.cleaned_data['to']
			from_field=form.cleaned_data['from_field']
			subject=form.cleaned_data['subject']
			body=form.cleaned_data['body']
			cli.send(to,from_field,subject,body)
			return render(request,'client/sent.html')
		else:
			return render(request,'client/compose.html',{'form':form})

def user_logout(request):
	logout(request)
	return redirect('/')
