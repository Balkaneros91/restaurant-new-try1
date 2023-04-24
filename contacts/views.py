from django.shortcuts import render
from .models import Contact

# Create your views here.


def contacts(request):
    contacts = Contact.objects.first()
    context = {
        'contacts': contacts
    }
    return render(request, 'contacts/contacts.html', context)
