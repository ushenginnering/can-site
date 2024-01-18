from django.urls import path
from .views import home, partner_view, signup_view, about_view, gallery_view, publication_view, giving_view, events_view, verify_giving_callback, meeting_view

urlpatterns = [
    path('', home, name='home'),
    path('partner/', partner_view, name='partner'),
    path('signup', signup_view, name='signup'),
    path('about_us/', about_view, name="about_us"),
    path('gallery/', gallery_view, name="gallery"),
    path('publications/', publication_view, name="publication"),
    path('giving/', giving_view, name="giving"),
    path('verify-giving/', verify_giving_callback, name="verify-giving"),
    path('events/', events_view, name="event"),
    path('meeting', meeting_view, name='meeting'),
]
