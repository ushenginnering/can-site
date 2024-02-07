from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class About(models.Model):
    organization_name            = models.CharField(max_length=50)
    organization_mailer_address  = models.EmailField(max_length=254)
    organization_mailer_password = models.CharField(max_length=100)
    body                         = models.TextField()

class Announcement(models.Model):
    image       = models.ImageField( upload_to='announcement', )
    headline    = models.CharField(max_length=100)
    body        = models.TextField()

    def __str__(self):
        return self.headline

class Gallery(models.Model):
    image       = models.ImageField( upload_to='gallery', )
    title       = models.CharField(max_length=100)
    body        = models.TextField()

    def __str__(self):
        return self.title

class Giving(models.Model):
    amount = models.PositiveIntegerField()
    message = models.TextField(null=True, blank=True)


class MeetingReport(models.Model):
    date = models.DateField()
    details = models.TextField()


    def __str__(self):
        return self.details[0: 10]
    
class Welfare(models.Model):
    member_name = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.member_name + ": " + self.details[0: 10]

class Publication(models.Model):
    image        = models.ImageField( upload_to='publication', )
    headline     = models.CharField(max_length=100)
    fontawesome_class      = models.CharField(max_length=50, default='fa-user-graduate')
    description  = models.TextField()
    file         = models.FileField(upload_to='publication_files')
    price        = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.headline
    
class PublicationPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.publication.headline}"
    

class Event(models.Model):
    title = models.CharField(max_length=80)
    banner = models.ImageField(upload_to='events')
    breif_description = models.CharField(max_length=200)
    event_date = models.DateTimeField()
    registration_start_date = models.DateField(blank=True)
    registration_end_date = models.DateField(blank=True)
    registration_url = models.URLField(max_length=200)

    def __str__(self):
        return self.title
    
