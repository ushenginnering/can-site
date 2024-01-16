from django.contrib import admin
from .models import Announcement, Gallery, Giving

# Register your models here.
admin.site.register(Announcement)
admin.site.register(Gallery)
admin.site.register(Giving)