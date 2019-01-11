from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        newUser = User(first_name=first_name,
                        last_name=last_name,
                        email=email,
                        username=username)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        messages.success(request, 'Kayıt Gerçekleştirildi.')
        return redirect('index')

    context = {'form' : form}
    return render(request, 'register.html', context)

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        'form' : form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        if user is None:
            messages.info(request, 'Kullanıcı Adı vey Parola Hatalı')
            return render(request, 'login.html', context)

        messages.success(request, 'Giriş Yapıldı')
        login(request, user)
        return redirect('index')

    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    messages.success(request, 'Çıkış Yapıldı')
    return redirect('index')