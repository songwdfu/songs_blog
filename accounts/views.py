from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def register_view(request):
      if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  user = form.save()
                  login(request, user)
                  messages.success(request, 'Your have successfully registered')
                  return redirect('home')
            else:
                  messages.error(request, 'Registration unsuccessful')
      else:
            form = UserCreationForm()
      return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
      if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                  username = form.cleaned_data.get('username')
                  password = form.cleaned_data.get('password')
                  user = authenticate(username=username, password=password)
                  if user is not None:
                        login(request, user)
                        messages.info(request, f'Welcome back, {username}!')
                        return redirect('home')
                  else:
                        messages.error(request, 'Incorrect username or password')
            else:
                  messages.error(request, 'Invalid username or password')
      else:
            form = AuthenticationForm()
      return render(request, 'accounts/login.html', {'form': form})