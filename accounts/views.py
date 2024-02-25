from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from accounts.form import UserRegistrationForm, UserLoginForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('about')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print(f"Authenticated user: {user.username}")
                login(request, user)
                return redirect('about')  
            else:
                print("Authentication failed. Invalid username or password.")
        else:
            print(form.errors)
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('about') 
