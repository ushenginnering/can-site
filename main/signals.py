from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from .models import MeetingReport

@receiver(post_save, sender=MeetingReport)
def send_meeting_report_email(sender, instance, **kwargs):
    subject = 'ChurchAriseNetwork New Meeting Report'
    message = f'A new meeting report has been saved:\n\n{instance.details}'
    admin_emails = [admin.email for admin in User.objects.filter(is_staff=True)]

    send_mail(subject, message, settings.EMAIL_HOST_USER, admin_emails, fail_silently=False)
    print('emails has been sent')
