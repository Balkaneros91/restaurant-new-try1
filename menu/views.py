from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Category, MenuItem


class MenuListView(ListView):
    model = MenuItem
    template_name = 'Menu/menu.html'
    context_object_name = 'menu_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


# def meal_details(request, slug):
#     meal_details = MenuItem.objects.get(slug=slug)

#     context = {'meal_details': meal_details}

#     return render(request, 'menu/meal_details.html', context)


class MealDetailsView(View):
    def get(self, request, slug, *args, **kwargs):
        meal_details = MenuItem.objects.get(slug=slug)
        context = {'meal_details': meal_details}
        return render(request, 'Menu/meal_details.html', context)
