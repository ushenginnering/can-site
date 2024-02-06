from django.shortcuts import render
from main.models import Publication, PublicationPayment


# Create your views here.
def publication_view(requests):
    context = {
        'publications': Publication.objects.all(),
    }
    print(Publication.objects.all())
    return render(requests, 'publications.html', context)