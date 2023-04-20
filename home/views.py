from django.shortcuts import render

# Create your views here.


def home_view(request):
    """ A view to return the index page"""

    context = {

    }

    return render(request, 'index.html', context)
