from django.urls import path
from .views import home, partner_view

urlpatterns = [
    path('', home, name='home'),
    path('partner/', partner_view, name='partner'),
]
