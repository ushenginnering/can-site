
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("", include('main.urls')),
    path("", include('user_authentication.urls')),
]
