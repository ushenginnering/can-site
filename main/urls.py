from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('partner/', views.partner_view, name='partner'),
    path('about/', views.about_view, name="about_us"),
    path('gallery/', views.gallery_view, name="gallery"),
    path('giving/', views.giving_view, name="giving"),
    path('events/', views.events_view, name="event"),
    path('meeting', views.meeting_view, name='meeting'),
    path('welfare', views.welfare_view, name='welfare'),
    path('admin_meeting_report', views.meeting_admin_view, name='meeting_admin'),
]
