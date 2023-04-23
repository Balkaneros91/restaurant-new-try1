"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import book_a_table, booking_confirmation


urlpatterns = [
    # path('', book_a_table, name='book_a_table'),
    path('book_a_table/', book_a_table, name='book_a_table'),
    path('booking_confirmation/', booking_confirmation, name='booking_confirmation'),

    # path('', book_a_table, name='book_table'),
    # path('booking_confirmation/', booking_confirmation, name='booking_confirmation'),

    # path('edit_booking/<int:booking_id>', edit_booking, name='edit_booking'),
    # path('delete_booking/<int:booking_id>/', delete_booking, name='delete_booking'),
]
