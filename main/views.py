from django.shortcuts import render

# Create your views here.


def home(requests):
    return render(requests, 'home.html')

def partner_view(requests):
    return render(requests, 'partner.html')