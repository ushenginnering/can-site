from django.contrib import admin
from .models import Announcement
from .models import Gallery

# Register your models here.
admin.site.register(Announcement)
admin.site.register(Gallery)