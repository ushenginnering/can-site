import django
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About, Announcement, Gallery, Giving, MeetingReport, Welfare, Publication

from .forms import AboutForm
from .Paystack import PayStack
import requests

# Create your views here.


def home(requests):
    context = {
        'announcements' : list(Announcement.objects.all()),
    }
    return render(requests, 'index.html', context)

def about_view(requests):
    return render(requests, 'aboutus.html')

def gallery_view(requests):
    context = {
        'gallery': Gallery.objects.all()
    }
    return render(requests, 'gallery.html', context)

def partner_view(requests):
    return render(requests, 'partners.html')

def meeting_view(request):
    if request.method == 'POST':
        meeting_report_date = request.POST.get('meetingDate')
        meeting_report_details = request.POST.get('meetingDetails')

        if not meeting_report_date or not meeting_report_details:
            messages.error(request, 'please fill in the date and details field accordinly')
            return redirect('/partner')
        
        messages.success(request, 'successfully saved meeting report and has been sent to all admins')
        MeetingReport.objects.create(date=meeting_report_date, details=meeting_report_details)

    return redirect('/partner')

def welfare_view(request):
    if request.method == 'POST':
        welfare_member_name = request.POST.get('memberName')
        welfare_report_details = request.POST.get('welfareDetails')

        if not welfare_member_name or not welfare_report_details:
            messages.error(request, 'please fill in the member\'s name and details field accordinly')
            return redirect('/partner')
        
        messages.success(request, 'successfully saved welfare report and has been sent to all admins')
        Welfare.objects.create(member_name=welfare_member_name, details=welfare_report_details)

    return redirect('/partner')

def publication_view(requests):
    context = {
        'publications': Publication.objects.all(),
    }
    print(Publication.objects.all())
    return render(requests, 'publications.html', context)

def giving_view(requests):
    if requests.method == 'POST':
        email = requests.user.email if requests.user.is_authenticated else "unknown@gmail.com"

        amount = int(requests.POST.get('amount'))
        message = requests.POST.get('message')

        redirect_url = PayStack.generate_checkout_url(email,  amount * 100)

        # save infor to database
        Giving.objects.create(amount = amount, message = message)
        return redirect(redirect_url)
    return render(requests, 'giving.html')

def verify_giving_callback(requests):
    reference = requests.GET.get('reference')
    messages.success(requests, 'Thanks for making donations, God sees and rewards openly')
    return redirect('/')

def events_view(requests):
    return render(requests, 'upcoming.html')


def login_view(requests):
    return render(requests, 'login.html')

def signup_view(requests):
    return render(requests, 'signup.html')