from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, MenuItem

# Create your views here.


class MenuListView(ListView):
    model = MenuItem
    template_name = 'menu.html'
    context_object_name = 'menu_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context