from django.contrib import admin
from .models import Announcement, Gallery, Giving, MeetingReport, Welfare, Publication, Event, PublicationPayment

# Register your models here.
admin.site.register(Announcement)
admin.site.register(Gallery)
admin.site.register(Giving)
admin.site.register(MeetingReport)
admin.site.register(Welfare)
admin.site.register(Publication)
admin.site.register(PublicationPayment)
admin.site.register(Event)