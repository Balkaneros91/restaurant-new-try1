from django.shortcuts import render
from .models import Contact, OpenHours

# Create your views here.


def contacts(request):
    contacts = Contact.objects.first()
    open_hours = OpenHours.objects.all()

    context = {
        'contacts': contacts,
        'open_hours': open_hours,
    }

    return render(request, 'contacts/contacts.html', context)
