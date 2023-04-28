from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Table, Booking

# Register your models here.


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_number', 'capacity')
    list_filter = ('capacity',)


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('name', 'number_of_guests', 'reservation_date_and_time', 'created_on', 'notes', 'approved')
    list_filter = ('reservation_date_and_time', 'approved',)
    search_fields = ['name', 'number_of_guests', 'reservation_date_and_time']
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)
