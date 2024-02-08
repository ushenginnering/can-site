from django.urls import path
from .views import publication_view, initiate_payment

urlpatterns = [
    path('', publication_view, name="publication"),
    path('purchase/<int:publication_id>/', initiate_payment, name="initiate_payment"),
]
