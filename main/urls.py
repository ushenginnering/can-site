from django.urls import path
from .views import home, partner_view, admin_view, login_view, signup_view

urlpatterns = [
    path('', home, name='home'),
    path('partner/', partner_view, name='partner'),
    path('admin', admin_view, name='admin'),
    path('login', login_view, name='login'),
    path('signup', signup_view, name='signup'),
]
