from django.urls import path
from .views import home, partner_view, admin_view, login_view, signup_view, about_us_submit_view

urlpatterns = [
    path('', home, name='home'),
    path('partner/', partner_view, name='partner'),
    path('admin', admin_view, name='admin'),
    path('signup', signup_view, name='signup'),
    path('about/', about_us_submit_view, name='about'),
]
