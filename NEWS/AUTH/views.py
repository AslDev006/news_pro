from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegister, UserEdit, ProfileEdit
from .models import Profile


def register_user(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(
                form.cleaned_data['password']
            )
            user.save()
            Profile.objects.create(user=user)
            return render(request, 'registration/register_done.html', {'user': user})
    else:
        form = UserRegister()
        return render(request, 'registration/register.html', {'form': form})

@login_required
def edit_user(request):
    if request.method == 'POST':
        user = UserEdit(request.POST, instance=request.user)
        profile = ProfileEdit(request.POST, request.FILES, instance=request.user.profile)
        if user.is_valid() and profile.is_valid():
            user.save()
            profile.save()
            return redirect('profile')
    else:
        user = UserEdit(instance=request.user)
        profile = ProfileEdit(instance=request.user.profile)

    return render(request, 'registration/profile_edit.html', {'user': user, 'profile': profile})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfully !!!')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in , try again....')
            return redirect('login')
    return render(request, 'registration/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You were logged out !!!')
    return redirect('home')

@login_required
def dashboard(request):
    user = request.user
    return render(request, 'registration/profile.html', {'user': user})