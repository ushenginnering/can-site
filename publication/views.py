from django.shortcuts import render, redirect, get_object_or_404
from main.models import Publication, PublicationPayment
from main.Paystack import PayStack

from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def publication_view(requests):

    publication_payments = []
    if requests.user.is_authenticated:
       publication_payments = PublicationPayment.objects.filter(user = requests.user).values_list('publication_id', flat=True)

    context = {
        'publications': Publication.objects.all(),
        'publication_payments': publication_payments,
        'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY,
    }
    return render(requests, 'publications.html', context)


def initiate_payment(request, publication_id):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('/login')
        
        publication = get_object_or_404(Publication, id=publication_id)
        publication_payment = PublicationPayment.objects.create(user = request.user, publication = publication)

        # Create payment on Paystack
        redirect_url = PayStack.generate_checkout_url(request.user.email,  publication.price * 100,
                                                       ref=publication_payment.id)
        
        return redirect(redirect_url)
    
def verify_payment(request):
    if request.method == 'POST':
        # Get reference from the callback data
        reference = request.POST.get('reference')

        # Verify the payment with Paystack
        # response = paystack_api.verify(reference)
        # status = response['data']['status']

        # # Handle payment status accordingly
        # if status == 'success':
        #     # Payment successful, update your database or perform other actions
        #     return JsonResponse({'status': 'success'})
        # else:
        #     # Payment failed or pending, handle as needed
        #     return JsonResponse({'status': 'failed'})