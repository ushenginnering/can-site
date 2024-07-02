from django.contrib.auth import views as auth_views
from django.urls import re_path, path
from django.core.mail import send_mail

from user_authentication import views

def send_email(request):
    send_mail(
        "Subject here",
        message="Here is the message.",
        from_email="send@churcharisenetwork.com.ng",
        recipient_list=["winninggodspower@gmail.com"],
        fail_silently=False)
    return {}

urlpatterns = [
    re_path('login/?', views.login_user, name='login'),
    re_path('signup/?', views.register, name='register'),
    re_path('logout/?', views.logout_user, name='logout'),
    re_path('send_mail', send_email),
    
    # path("password_reset", views.password_reset_request, name="password_reset")
    path("password_reset/", views.CustomPasswordResetView.as_view(template_name="password/password_reset.html"), name='password_reset'),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_done.html"), name='password_reset_done'),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_complete.html"), name='password_reset_complete'),
]