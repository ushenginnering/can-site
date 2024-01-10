from django.db import models

# Create your models here.
class About(models.Model):
    organization_name            = models.CharField(max_length=50)
    organization_mailer_address  = models.EmailField(max_length=254)
    organization_mailer_password = models.CharField(max_length=100)
    body                         = models.TextField()
