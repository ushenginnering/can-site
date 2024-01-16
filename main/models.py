from django.db import models

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
    message = models.TextField(empty=True, blank=True)
    