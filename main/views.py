from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def home(requests):
    return render(requests, 'home.html')

def partner_view(requests):
    return render(requests, 'partner.html')

def admin_view(requests):
    if requests.user.is_authenticated and requests.user.is_superuser:
        return render(requests, 'admin.html')
    else:
        messages.error(requests, 'you don\'nt have permission to visit the page')
        return redirect('/')

def login_view(requests):
    return render(requests, 'login.html')

def signup_view(requests):
    return render(requests, 'signup.html')