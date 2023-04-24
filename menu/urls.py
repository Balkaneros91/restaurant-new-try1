from django.urls import path
from .views import MenuListView


urlpatterns = [
    path('', MenuListView.as_view(), name='menu'),
    # path('<slug:slug>', meal_details, name='meal_details')
]
