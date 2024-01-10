import django
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import AboutForm

# Create your views here.


def home(requests):
    return render(requests, 'home.html')

def partner_view(requests):
    return render(requests, 'partner.html')

def admin_view(requests, about_form=None):
    if requests.user.is_authenticated and requests.user.is_superuser:
        about_info = About.objects.first()
        
        context = {
            'about_us' : {
                'organization_name': about_info.organization_name if about_info else '',
                'organization_mailer_address': about_info.organization_mailer_address if about_info else '',
                'organization_mailer_password': about_info.organization_mailer_password if about_info else '',
                'body': about_info.body if about_info else '',
            },
            'about_form': about_form or AboutForm(),
        }

        return render(requests, 'admin.html', context)
    else:
        messages.error(requests, 'you don\'nt have permission to visit the page')
        return redirect('/')

def about_us_submit_view(requests):
    if requests.method == "POST":
        about_form = AboutForm(requests.POST)
        if about_form.is_valid():
            about_model = about_form.save(commit=False)
            about_model.id = 1
            about_model.save()
            return redirect('/admin')
        else:
            # Pass the form with errors to admin_view
            return admin_view(requests, about_form=about_form)

    return redirect('/admin')

def login_view(requests):
    return render(requests, 'login.html')

def signup_view(requests):
    return render(requests, 'signup.html')