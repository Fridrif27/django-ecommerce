from django.shortcuts import render


def login(request):
    context = {
        'title': 'Home - login'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Home - registration'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Home - profile'
    }
    return render(request, 'users/profile.html', context)


def logout(request):