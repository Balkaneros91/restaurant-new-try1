from django.contrib import admin
from .models import Table, Booking

# Register your models here.


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_number', 'capacity')
    list_filter = ('capacity',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'table', 'name', 'number_of_guests', 'notes')
    list_filter = ('name', 'email', 'date',)
