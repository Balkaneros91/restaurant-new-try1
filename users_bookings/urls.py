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
from .views import booking_list, booking_edit, booking_delete


# urlpatterns = [
#     path('', booking_list, name='booking_list'),
#     path('booking_list/', booking_list, name='booking_list'),
#     path('booking_edit/<int:id>/', booking_edit, name='booking_edit'),
#     path('booking_delete/<int:id>/', booking_delete, name='booking_delete'),
# ]

urlpatterns = [
    # path('', booking_list, name='booking_list'),
    path('booking_list/', booking_list, name='booking_list'),
    path('booking_list/<int:pk>/edit/', booking_edit, name='booking_edit'),
    path('booking_list/<int:pk>/delete/', booking_delete, name='booking_delete'),
]
