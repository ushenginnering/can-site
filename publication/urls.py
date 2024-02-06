from django.urls import path
from .views import publication_view

urlpatterns = [
    path('', publication_view, name="publication"),
]
