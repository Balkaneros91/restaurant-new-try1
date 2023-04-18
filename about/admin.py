from django.contrib import admin
from .models import AboutUs


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):

    list_display = ('restaurant_name', 'description')
