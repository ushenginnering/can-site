import os
import subprocess
from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse
from django.contrib import messages

# modules needed for user authentication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#for pasword reset
from django.contrib.auth import views
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.views import PasswordResetView

from django.conf import settings

# importing the use model
from django.contrib.auth import get_user_model
User = get_user_model()


# importing the forms
from .forms import LoginForm, RegisterForm

# routes for user registration
def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            # form.save only works when form is created from a model
            form.save()
            messages.success(request, 'succesfully created account')
            return redirect('/')
        else:
            # rendering the template again if the form is not valid with the prepopulated data.
            return render(request, 'signup.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
    

def login_user(request):
    # redirect user to home if already logged in
    if request.user.is_authenticated:
        messages.info(request, 'You Are Already Logged In')
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = User.objects.filter(email = form.cleaned_data.get('email')).first()
            print(username)
            # the authenticate function returns the user object if the user is found else it returns none
            user = authenticate(username=username, password=form.cleaned_data.get('password'))
            if user:
                login(request, user)
                messages.success(request, f'successfully logged in as {user.username}')
                return redirect('/partner/')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('/login')

        # if form is not valid render the template again with pre populated data
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def login_admin_user(request):
    # redirect user to home if already logged in
    if request.user.is_authenticated:
        messages.info(request, 'You Are Already Logged In')
        return redirect('/admin')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            username = User.objects.filter(email = form.cleaned_data.get('email')).first()
            # the authenticate function returns the user object if the user is found else it returns none
            user = authenticate(username=username, password=form.cleaned_data.get('password'))
            if user and user.is_superuser:
                login(request, user)
                messages.success(request, f'successfully logged in as {user.username}')
                return redirect('/admin')
            else:
                messages.error(request, 'Invalid credentials')
                # form.add_error('user not found')
                return redirect('/login')

        # if form is not valid render the template again with pre populated data
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'successfully logged out')
        return redirect('/')
    else:
        messages.info(request, 'you\re already logged out')
        return redirect('/')
        

class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        user_email = form.cleaned_data['email']

        associated_user = User.objects.filter(Q(email=user_email))
        if not associated_user.exists():
            messages.error(self.request, 'Email not found. please create an acount')
            return redirect(resolve_url('login'))
        
        user = associated_user.first()
        context = {
            'email': user_email,
            'domain': self.request.META['HTTP_HOST'],
            'site_name': settings.SITE_NAME,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'user': user,
            'token': default_token_generator.make_token(user),
            'protocol': 'https' if self.request.is_secure() else 'http',
        }
        subject = 'Password Reset'
        message = render_to_string(self.email_template_name, context)

        # Call the PHP script
        self.send_email_via_php(subject, message, user_email)

        return super().form_valid(form)

    def send_email_via_php(self, subject, message, recipient_email):
        print(os.path.join(settings.BASE_DIR, 'send_email.php'))
        try:
            result = subprocess.run(
                ['php', os.path.join(settings.BASE_DIR, 'send_email.php'), subject, message, recipient_email],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                raise Exception(f"Failed to send email: {result.stderr}")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")