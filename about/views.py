from django.shortcuts import render
from .models import AboutUs

# Create your views here.


def about_us(request):
    about_us = AboutUs.objects.first()  # or use a specific object if you have multiple
    context = {
        'about_us': about_us
    }
    return render(request, 'about_us.html', context)
