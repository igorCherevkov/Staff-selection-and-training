from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserProfileForm, UserRegistrationForm, UserLoginForm, CreateResume
from users.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from companies.models import Company


def userLogin(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('mainPage'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Вход',
        'form': form
    }
    return render(request, 'users/userLogin.html', context)


def userRegistration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            user = User()
            user.username = request.POST['username']
            password = request.POST['password2']
            user.set_password(password)
            user.save()
            return HttpResponseRedirect(reverse('users:userLogin'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'users/userRegistration.html', context)


@login_required
def userLogout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainPage'))


@login_required
def userProfile(request):
    try:
        owner = Company.objects.get(owner_id = request.user.username)
    except:
        owner = None
    try:
        staff = Company.objects.get(owner_id = request.user.username)
    except:
        staff = None
    if request.method == 'POST':
        form = UserProfileForm(instance = request.user, data = request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:userProfile'))
    else:
        form = UserProfileForm(instance = request.user)
    if owner:
        context = {
        'title': 'Профиль',
        'form': form,
        'owner': True
    }
    elif staff:
        context = {
        'title': 'Профиль',
        'form': form,
        'staff': True
    }
    else:
        context = {
            'title': 'Профиль',
            'form': form,
            'owner': False,
            'staff': False
        }
    return render(request, 'users/userProfile.html', context)


@login_required
def createResume(request):
    try:
        owner = Company.objects.get(owner_id = request.user.username)
    except:
        owner = None
    try:
        staff = Company.objects.get(owner_id = request.user.username)
    except:
        staff = None
    if request.method == 'POST':
        form = CreateResume(instance = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:userProfile'))
    else:
        form = CreateResume()
    if owner:
        context = {
        'title': 'Создание резюме',
        'form': form,
        'owner': True
    }
    elif staff:
        context = {
        'title': 'Создание резюме',
        'form': form,
        'staff': True
    }
    else:
        context = {
            'title': 'Создание резюме',
            'form': form,
            'owner': False,
            'staff': False
        }
    return render(request, 'users/createResume.html', context)