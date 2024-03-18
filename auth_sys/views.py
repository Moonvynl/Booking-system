from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect
from auth_sys.forms import CustomCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomCreationForm()

    return render(
        request,
        'auth_sys/register.html', 
        context = {"form" : form}
    )

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.error(request, 'Якийсь другий текст')
                return redirect('home')
            else:
                messages.error(request, 'Якийсь текст')

    else:
        form = AuthenticationForm()

    return render(
        request,
        'auth_sys/login.html', 
        context = {"form" : form}
        )











