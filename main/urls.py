from django.urls import path
from .views import home, partner_view, admin_view, signup_view, about_us_submit_view, about_view, gallery_view, publication_view, giving_view, events_view, verify_giving_callback

urlpatterns = [
    path('', home, name='home'),
    path('partner/', partner_view, name='partner'),
    path('admin', admin_view, name='admin'),
    path('signup', signup_view, name='signup'),
    path('about/', about_us_submit_view, name='about'),
    path('about_us/', about_view, name="about_us"),
    path('gallery/', gallery_view, name="gallery"),
    path('publications/', publication_view, name="publication"),
    path('giving/', giving_view, name="giving"),
    path('verify-giving/', verify_giving_callback, name="verify-giving"),
    path('events/', events_view, name="event"),
]
