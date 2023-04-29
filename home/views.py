from django.shortcuts import render
from menu.models import Category, MenuItem
from about.models import AboutUs
from contacts.models import Contact, OpenHours

# Create your views here.


def home_view(request):
    """ A view to return the index page"""

    categories = Category.objects.all()
    meals = MenuItem.objects.all()
    meal_list = MenuItem.objects.all()
    about_us = AboutUs.objects.last()
    contacts = Contact.objects.last()
    open_hours = OpenHours.objects.all()

    context = {
        'categories': categories,
        'meals': meals,
        'meal_list': meal_list,
        'about_us': about_us,
        'contacts': contacts,
        'open_hours': open_hours,
    }

    return render(request, 'home/index.html', context)
