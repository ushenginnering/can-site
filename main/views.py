from django.shortcuts import render

# Create your views here.


def home(requests):
    return render(requests, 'home.html')

def partner_view(requests):
    return render(requests, 'partner.html')

def admin_view(requests):
    return render(requests, 'admin.html')

def login_view(requests):
    return render(requests, 'login.html')

def signup_view(requests):
    return render(requests, 'signup.html')