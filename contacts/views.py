from django.shortcuts import render
from .models import Contact


def contacts(request):
    contacts = Contact.objects.first()
    context = {
        'contacts': contacts
    }
    return render(request, 'contacts/contacts.html', context)
