from django.contrib import admin
from .models import AboutUs

# Register your models here.


# admin.site.register(AboutUs, AboutUsAdmin)
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('restaurant_name', 'description')
