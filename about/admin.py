from django.contrib import admin
from .models import AboutUs, ThingsWeOffer


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):

    list_display = ('restaurant_name', 'description')


@admin.register(ThingsWeOffer)
class ThingsWeOfferAdmin(admin.ModelAdmin):

    list_display = ('title', 'description')
